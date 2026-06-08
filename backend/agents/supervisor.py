import logging
from typing import Dict, Any
from backend.models.data_models import AgentMessageLog

logger = logging.getLogger("SupervisorAgent")

class SupervisorAgent:
    def __init__(self):
        self.name = "Supervisor Agent"
        self.goal = "Coordinate the TenderPilot workforce pipeline, handle runtime exceptions, manage organizational memory databases, and verify bid milestones."
        self.status = "Idle"
        self.reasoning = ""
        self.inputs = {}
        self.outputs = {}
        self.confidence_score = 1.0

    def coordinate_next_step(self, workflow_state: Dict[str, Any], target_agent: str) -> AgentMessageLog:
        self.status = f"RoutingTo_{target_agent.replace(' ', '')}"
        self.inputs = {
            "workflow_id": workflow_state.get("workflow_id"),
            "target_agent": target_agent
        }
        self.reasoning = f"Determining the next operation step in the bid generation lifecycle. Routing execution thread to {target_agent}."
        
        self.outputs = {
            "status": "Routed",
            "coordination_channel": "SemanticKernelChannel"
        }
        self.confidence_score = 1.0
        self.reasoning = f"Handing over execution thread parameters to the '{target_agent}' agent to execute its allocated role."
        
        return AgentMessageLog(
            agent_name=self.name,
            goal=self.goal,
            status=self.status,
            reasoning=self.reasoning,
            inputs=self.inputs,
            outputs=self.outputs,
            confidence_score=self.confidence_score
        )
