import uuid
import logging
from typing import Dict, Any, List
from datetime import datetime
from backend.models.data_models import WorkflowState, AgentMessageLog, TenderAlert, HumanApprovalItem, ProposalDraft, ProposalSection
from backend.memory.cosmos_store import CosmosStore
from backend.memory.graph_store import GraphStore
from backend.agents.supervisor import SupervisorAgent
from backend.agents.discovery import DiscoveryAgent
from backend.agents.eligibility import EligibilityAgent
from backend.agents.research import ResearchAgent
from backend.agents.competitor_intel import CompetitorIntelAgent
from backend.agents.planner import ProposalPlannerAgent
from backend.agents.generator import ProposalGeneratorAgent
from backend.agents.execution import ExecutionAgent
from backend.agents.reflection import ReflectionAgent

logger = logging.getLogger("TenderOrchestrator")

class WorkflowOrchestrator:
    def __init__(self, db_store: CosmosStore, graph_store: GraphStore):
        self.db = db_store
        self.graph = graph_store
        
        # Instantiate agents
        self.supervisor = SupervisorAgent()
        self.discovery = DiscoveryAgent()
        self.eligibility = EligibilityAgent()
        self.research = ResearchAgent()
        self.competitor_intel = CompetitorIntelAgent()
        self.planner = ProposalPlannerAgent()
        self.generator = ProposalGeneratorAgent()
        self.execution = ExecutionAgent()
        self.reflection = ReflectionAgent()

    def start_pipeline(self, portal_url: str, query: str) -> WorkflowState:
        workflow_id = f"wf_tender_{uuid.uuid4().hex[:8]}"
        tender_id = "CPPP/AI-ANALYSIS/2026/089"
        
        state = WorkflowState(
            workflow_id=workflow_id,
            tender_id=tender_id,
            current_step=1,
            status="Running",
            logs=[],
            autonomy_score=100.0
        )
        
        # STEP 1: User Query / System Trigger
        log1 = AgentMessageLog(
            agent_name="System Gateway",
            goal="Scan tender portals based on query constraints.",
            status="Triggered",
            reasoning=f"Initiating scheduled crawl loop matching user parameters: '{query}'.",
            inputs={"portal": portal_url, "query": query},
            outputs={"trigger": "UserRequest"},
            confidence_score=1.0
        )
        state.logs.append(log1)
        self.db.save_workflow(state)
        
        # Execute remaining steps up to the Human Approval checkpoint
        state = self.run_to_approval(state, portal_url, query)
        return state

    def run_to_approval(self, state: WorkflowState, portal_url: str, query: str) -> WorkflowState:
        # STEP 2: Discovery Agent scans portals
        state.current_step = 2
        sup_log = self.supervisor.coordinate_next_step(state.model_dump(), "Discovery Agent")
        state.logs.append(sup_log)
        
        disc_log = self.discovery.run(portal_url, query)
        state.logs.append(disc_log)
        
        disc_data = disc_log.outputs
        tender = TenderAlert(
            id=state.tender_id,
            title=disc_data["title"],
            portal=disc_data["portal"],
            budget=disc_data["budget"],
            publish_date=disc_data["publish_date"],
            close_date=disc_data["close_date"],
            scraped_text=disc_data["source_text"],
            status="Discovered"
        )
        self.db.save_tender(tender)
        
        # STEP 3: Eligibility Agent runs criteria checks
        state.current_step = 3
        sup_log = self.supervisor.coordinate_next_step(state.model_dump(), "Eligibility Agent")
        state.logs.append(sup_log)
        
        elig_log = self.eligibility.run(tender.model_dump())
        state.logs.append(elig_log)
        
        # STEP 4: Scores computed
        state.current_step = 4
        elig_outputs = elig_log.outputs
        tender.eligibility_score = elig_outputs["eligibility_score"]
        tender.tender_match_score = elig_outputs["tender_match_score"]
        tender.win_probability = elig_outputs["win_probability"]
        tender.eligibility_status = elig_outputs["eligibility_status"]
        tender.status = "Evaluated"
        self.db.save_tender(tender)
        
        log_scores = AgentMessageLog(
            agent_name="Tender Match Engine",
            goal="Calculate match scoring benchmarks.",
            status="ScoresGenerated",
            reasoning="Evaluating technical budget fit and team parameters.",
            inputs=elig_outputs,
            outputs={
                "tender_match_score": tender.tender_match_score,
                "eligibility_score": tender.eligibility_score,
                "win_probability": tender.win_probability
            },
            confidence_score=1.0
        )
        state.logs.append(log_scores)
        
        # STEP 5: Research Agent (RAG past bids)
        state.current_step = 5
        sup_log = self.supervisor.coordinate_next_step(state.model_dump(), "Research Agent")
        state.logs.append(sup_log)
        
        res_log = self.research.run(tender.title)
        state.logs.append(res_log)
        tender.historical_citations = res_log.outputs["historical_references"]
        self.db.save_tender(tender)
        
        # STEP 6: Competitor Intelligence Agent
        state.current_step = 6
        sup_log = self.supervisor.coordinate_next_step(state.model_dump(), "Competitor Intelligence Agent")
        state.logs.append(sup_log)
        
        comp_log = self.competitor_intel.run(tender.title)
        state.logs.append(comp_log)
        
        from backend.models.data_models import CompetitorProfile
        tender.previous_winners = [CompetitorProfile(**c) for c in comp_log.outputs["previous_winners"]]
        self.db.save_tender(tender)
        
        # STEP 7: Proposal Planner Agent
        state.current_step = 7
        sup_log = self.supervisor.coordinate_next_step(state.model_dump(), "Proposal Planner Agent")
        state.logs.append(sup_log)
        
        plan_log = self.planner.run(tender.id, elig_outputs)
        state.logs.append(plan_log)
        
        from backend.models.data_models import ComplianceTask
        tender.roadmap = [ComplianceTask(**t) for t in plan_log.outputs["roadmap"]]
        self.db.save_tender(tender)
        
        # STEP 8: Proposal Generator Agent
        state.current_step = 8
        sup_log = self.supervisor.coordinate_next_step(state.model_dump(), "Proposal Generator Agent")
        state.logs.append(sup_log)
        
        gen_log = self.generator.run(tender.title, elig_outputs["requirements_extracted"])
        state.logs.append(gen_log)
        tender.proposal = ProposalDraft(**gen_log.outputs["proposal_draft"])
        self.db.save_tender(tender)
        
        # STEP 9: Execution Agent (Drafts Outlook & Planner cards)
        state.current_step = 9
        sup_log = self.supervisor.coordinate_next_step(state.model_dump(), "Execution Agent")
        state.logs.append(sup_log)
        
        exec_log = self.execution.run(plan_log.outputs["roadmap"], tender.title)
        state.logs.append(exec_log)
        
        # STEP 10: Reflection Agent (Citations verification)
        state.current_step = 10
        sup_log = self.supervisor.coordinate_next_step(state.model_dump(), "Reflection Agent")
        state.logs.append(sup_log)
        
        ref_log = self.reflection.run(state.logs)
        state.logs.append(ref_log)
        
        # STEP 11: Human Approval Checkpoint
        state.current_step = 11
        state.status = "AwaitingApproval"
        
        approval = HumanApprovalItem(
            approval_id=f"apv_{state.workflow_id}",
            tender_id=state.tender_id,
            staged_email=exec_log.outputs["staged_actions"][0],
            staged_tasks=exec_log.outputs["staged_actions"][1:],
            staged_proposal=gen_log.outputs["proposal_draft"]
        )
        self.db.save_approval(approval)
        
        state.autonomy_score = 100.0
        self.db.save_workflow(state)
        
        return state

    def complete_pipeline(self, workflow_id: str, action: str, feedback: str = "") -> WorkflowState:
        state = self.db.get_workflow(workflow_id)
        if not state or state.status != "AwaitingApproval":
            raise ValueError("Workflow is not pending human validation approval.")
            
        approval = self.db.get_approval(f"apv_{workflow_id}")
        tender = self.db.get_tender(state.tender_id)
        
        # STEP 11: Governance Response Processed
        state.current_step = 11
        human_status = "Approved" if action == "approve" else "Modified" if action == "modify" else "Rejected"
        
        approval.status = human_status
        approval.reviewed_at = datetime.utcnow()
        approval.reviewer_comments = feedback
        self.db.save_approval(approval)
        
        log_human = AgentMessageLog(
            agent_name="Human Approval Layer",
            goal="Provide governance review of proposal parameters and staged actions.",
            status=human_status,
            reasoning=f"Human reviewer finalized audit. Status: {action.upper()}. Review feedback: '{feedback}'",
            inputs={"approval_id": approval.approval_id, "staged_email": approval.staged_email},
            outputs={"resolution": action},
            confidence_score=1.0
        )
        state.logs.append(log_human)

        if action in ["approve", "modify"]:
            # STEP 12: Supervisor Agent Executes approved Microsoft Graph Actions
            state.current_step = 12
            sup_log = self.supervisor.coordinate_next_step(state.model_dump(), "Execution Agent (Publishing)")
            state.logs.append(sup_log)
            
            exec_log = AgentMessageLog(
                agent_name="Execution Agent",
                goal="Dispatch staged tasks and communications.",
                status="Executed",
                reasoning="Transmitting staged email draft and Planner milestones following human release.",
                inputs={"email": approval.staged_email},
                outputs={"outlook_drafts_posted": 1, "planner_tasks_created": len(approval.staged_tasks)},
                confidence_score=1.0
            )
            state.logs.append(exec_log)
            
            # STEP 13: Conclude and Update Knowledge Graph
            state.current_step = 13
            self._update_knowledge_graph(tender)
            
            state.status = "Completed"
            tender.status = "Completed"
            self.db.save_tender(tender)
            
            state.autonomy_score = 91.0 if action == "approve" else 84.0
            
            log_completion = AgentMessageLog(
                agent_name="Supervisor Agent",
                goal="Conclude operations run.",
                status="Finished",
                reasoning="Proposal draft finalized, Microsoft 365 cards published, and Knowledge Graph updated.",
                inputs={},
                outputs={"autonomy_score": state.autonomy_score},
                confidence_score=1.0
            )
            state.logs.append(log_completion)
        else:
            # Rejection
            state.status = "Failed"
            state.current_step = 13
            state.autonomy_score = 50.0
            tender.status = "Rejected"
            self.db.save_tender(tender)
            
            log_completion = AgentMessageLog(
                agent_name="Supervisor Agent",
                goal="Aborted workflow.",
                status="Aborted",
                reasoning="Human reviewer rejected the staged bid roadmap.",
                inputs={},
                outputs={"status": "Aborted"},
                confidence_score=1.0
            )
            state.logs.append(log_completion)
            
        self.db.save_workflow(state)
        return state

    def _update_knowledge_graph(self, tender: TenderAlert):
        # Add Tender node
        self.graph.add_node(tender.id, "Tender", tender.title, {"budget": tender.budget, "match_score": tender.tender_match_score})
        
        # Link Tender to portals
        portal_node = "portal_gem" if "gem" in tender.portal.lower() else "portal_cppp"
        self.graph.add_relationship(f"e_port_{tender.id}", tender.id, portal_node, "SIBLING_OF")
        
        # Link Tender to Business Development Dept
        self.graph.add_relationship(f"e_dept_{tender.id}", tender.id, "dept_sales", "ASSIGNED_TO")
        
        # Add Competitors and link as rivals
        for competitor in tender.previous_winners:
            comp_id = f"comp_{competitor.name.lower().replace(' ', '_')}"
            self.graph.add_node(comp_id, "Competitor", competitor.name, {"avg_bid": competitor.avg_bid_amount})
            self.graph.add_relationship(f"e_comp_{tender.id}_{comp_id}", tender.id, comp_id, "COMPETES_WITH")
            
        # Add tasks nodes
        for task in tender.roadmap:
            self.graph.add_node(task.task_id, "Task", task.title, {"due": task.deadline, "role": task.assigned_role})
            self.graph.add_relationship(f"e_tsk_ref_{task.task_id}", task.task_id, tender.id, "RESOLVES")
            
        logger.info(f"Knowledge Graph updated for Tender: {tender.id}")
