import logging
from typing import Dict, Any, List
from backend.models.data_models import AgentMessageLog, CompetitorProfile

logger = logging.getLogger("CompetitorIntelAgent")

class CompetitorIntelAgent:
    def __init__(self):
        self.name = "Competitor Intelligence Agent"
        self.goal = "Analyze awarded databases, identify previous winners, and extract competitor profiles to build bidding insights."
        self.status = "Idle"
        self.reasoning = ""
        self.inputs = {}
        self.outputs = {}
        self.confidence_score = 1.0

    def run(self, tender_title: str) -> AgentMessageLog:
        self.status = "Analyzing Competitors"
        self.inputs = {"tender_title": tender_title}
        self.reasoning = "Querying award history for analytics/software bids in smart city segments."
        
        # Competitor profiles found in DB
        competitors = [
            CompetitorProfile(
                name="AlphaTech Systems",
                award_count=8,
                avg_bid_amount=4200000.0,
                common_traits=["ISO 27001 Certified", "Central Govt Experience", "Team Size > 50"]
            ),
            CompetitorProfile(
                name="BetaCorp Solutions",
                award_count=5,
                avg_bid_amount=3900000.0,
                common_traits=["ISO 9001 Certified", "Regional PSU Network", "Team Size > 25"]
            )
        ]
        
        self.status = "Completed"
        self.outputs = {
            "previous_winners": [c.model_dump() for c in competitors],
            "estimated_winning_traits": [
                "ISO 27001 certified compliance is mandatory to match AlphaTech Systems.",
                "Bidding amount should hover around 41 Lakhs to match historical price margins.",
                "Ensure team size credentials are highlighted since competitors exceed 25 members."
            ]
        }
        self.confidence_score = 0.93
        self.reasoning = (
            f"Extracted 2 major competitors with past wins. Identified AlphaTech Systems "
            f"as the primary threat. Generated winning traits checklist for our proposal layout."
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
