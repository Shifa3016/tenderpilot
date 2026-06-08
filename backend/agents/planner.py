import logging
from typing import Dict, Any, List
from backend.models.data_models import AgentMessageLog, ComplianceTask

logger = logging.getLogger("ProposalPlannerAgent")

class ProposalPlannerAgent:
    def __init__(self):
        self.name = "Proposal Planner Agent"
        self.goal = "Create bid proposal roadmap, list missing documents, and structure prep tasks for internal teams."
        self.status = "Idle"
        self.reasoning = ""
        self.inputs = {}
        self.outputs = {}
        self.confidence_score = 1.0

    def run(self, tender_id: str, eligibility_outputs: Dict[str, Any]) -> AgentMessageLog:
        self.status = "Planning"
        self.inputs = {
            "tender_id": tender_id,
            "eligibility_outputs": eligibility_outputs
        }
        self.reasoning = "Formulating workflow timelines and checklists matching tender qualification clauses."
        
        # Structure bid prep checklist
        tasks = [
            ComplianceTask(
                task_id="tsk_001",
                title="Assemble ISO 27001 Certification PDF",
                description="Retrieve active ISO certificate from IT Security vaults and prepare attachment.",
                assigned_role="Compliance lead",
                deadline="2026-06-15"
            ),
            ComplianceTask(
                task_id="tsk_002",
                title="Compile Case Study of Smart Irrigation project",
                description="Format historical smart irrigation metrics as a past performance credential document.",
                assigned_role="Engineering Director",
                deadline="2026-06-18"
            ),
            ComplianceTask(
                task_id="tsk_003",
                title="Draft Financial Bid Worksheet",
                description="Compile project cost matrices and set bid price around 41 Lakhs for pricing competitiveness.",
                assigned_role="Finance Controller",
                deadline="2026-06-22"
            ),
            ComplianceTask(
                task_id="tsk_004",
                title="Consolidate Technical Architecture Writeup",
                description="Review systems topology, security parameters, and data pipelines description.",
                assigned_role="Principal Architect",
                deadline="2026-06-24"
            )
        ]
        
        self.status = "Completed"
        self.outputs = {
            "roadmap": [t.model_dump() for t in tasks],
            "total_tasks": len(tasks),
            "critical_milestone": "ISO 27001 document collection"
        }
        self.confidence_score = 0.95
        self.reasoning = (
            f"Successfully structured a 4-step bid preparation roadmap for Tender {tender_id}. "
            f"Set priority on collecting the ISO 27001 credential to match previous winner benchmarks."
        )
        
        return AgentMessageLog(
            agent_name=self.name,
            goal=self.goal,
            status=self.status,
            reasoning=self.reasoning,
            inputs=self.inputs,
            outputs=self.outputs,
            confidence_score=self.confidence_score
        )
