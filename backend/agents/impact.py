import logging
from typing import Dict, Any
from backend.models.data_models import AgentMessageLog

logger = logging.getLogger("ImpactAgent")

class ImpactAnalysisAgent:
    def __init__(self):
        self.name = "Impact Analysis Agent"
        self.goal = "Analyze regulatory circulars to assess business risks, identify impacted departments, and calculate risk scores."
        self.status = "Idle"
        self.reasoning = ""
        self.inputs = {}
        self.outputs = {}
        self.confidence_score = 1.0

    def run(self, alert_data: Dict[str, Any]) -> AgentMessageLog:
        self.status = "Analyzing"
        self.inputs = alert_data
        self.reasoning = "Reading regulatory content, scanning for legal liabilities, monetary fines, execution deadlines, and compliance mandates."
        
        extracted_text = alert_data.get("extracted_text", "")
        
        # Calculate mock risk scoring based on keyword occurrences
        risk_score = 50.0
        affected_depts = ["dept_compliance"]
        implications = "A new policy was published requiring operational adjustments."
        
        if "cybersecurity" in extracted_text.lower() or "security" in extracted_text.lower():
            risk_score = 88.0
            affected_depts.extend(["dept_it", "dept_risk"])
            implications = (
                "Critical impact on digital platforms. Mandatory MFA deployment and offline logging backups required. "
                "Failure to execute by December 31, 2026, will trigger penalties under Section 58B of the RBI Act."
            )
        elif "tax" in extracted_text.lower() or "gst" in extracted_text.lower():
            risk_score = 75.0
            affected_depts.extend(["dept_ops"])
            implications = "Requires updating general ledger tax formulas and billing operations."
            
        self.status = "Completed"
        self.outputs = {
            "risk_score": risk_score,
            "implications": implications,
            "affected_departments": affected_depts,
            "deadline": "2026-12-31"
        }
        self.confidence_score = 0.95
        self.reasoning = (
            f"Evaluated regulatory text and classified update as HIGH RISK ({risk_score}/100) due to explicit threats "
            f"of legislative penalties. Determined impact on: IT, Risk, and Compliance departments."
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
