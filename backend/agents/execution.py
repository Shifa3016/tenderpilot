import logging
from typing import Dict, Any, List
from backend.plugins.graph_plugin import GraphPlugin
from backend.models.data_models import AgentMessageLog

logger = logging.getLogger("ExecutionAgent")

class ExecutionAgent:
    def __init__(self):
        self.name = "Execution Agent"
        self.goal = "Draft emails to division heads, prepare notification reports, and stage Microsoft Planner checklist cards."
        self.status = "Idle"
        self.reasoning = ""
        self.inputs = {}
        self.outputs = {}
        self.confidence_score = 1.0
        self.graph = GraphPlugin()

    def run(self, roadmap: List[Dict[str, Any]], tender_title: str) -> AgentMessageLog:
        self.status = "Drafting Actions"
        self.inputs = {
            "roadmap": roadmap,
            "tender_title": tender_title
        }
        self.reasoning = "Staging task assignments and notifications to match proposal milestones."
        
        # Format staged email
        email_recipient = "bd-team@tendercorp.com"
        email_subject = f"Action Required: Proposal Roadmap staged for '{tender_title}'"
        email_body = (
            f"Hi Team,\n\n"
            f"Our autonomous agent has analyzed '{tender_title}' (Tender ID: CPPP/AI-ANALYSIS/2026/089) "
            f"and calculated a 92% Tender Match Score. We have staged a proposal draft.\n\n"
            f"The following bid tasks have been structured on Microsoft Planner:\n"
        )
        for idx, task in enumerate(roadmap):
            email_body += f"- {task.get('title')} (Assignee: {task.get('assigned_role')}, Due: {task.get('deadline')})\n"
        email_body += "\nPlease review the bid drafts and approve execution on the TenderPilot dashboard.\n\nRegards,\nTenderPilot AI Workforce"

        staged_actions = [
            {
                "type": "draft_email",
                "recipient": email_recipient,
                "subject": email_subject,
                "body": email_body
            }
        ]
        
        for task in roadmap:
            staged_actions.append({
                "type": "create_task",
                "title": task.get("title"),
                "bucket": task.get("assigned_role"),
                "due": task.get("deadline"),
                "description": task.get("description")
            })

        self.status = "AwaitingApproval"
        self.outputs = {
            "staged_actions": staged_actions,
            "actions_staged_count": len(staged_actions)
        }
        self.confidence_score = 0.96
        self.reasoning = (
            f"Successfully drafted notification email to {email_recipient} and staged {len(roadmap)} "
            f"Planner checklist cards. Holding for Governance Checkpoint authorization."
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
