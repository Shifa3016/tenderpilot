import logging
from typing import Dict, Any
from backend.rag.search_service import RAGSearchService
from backend.models.data_models import AgentMessageLog

logger = logging.getLogger("ResearchAgent")

class ResearchAgent:
    def __init__(self):
        self.name = "Research Agent"
        self.goal = "Retrieve historical tender templates, similar projects, and RAG index data for grounding the proposal."
        self.status = "Idle"
        self.reasoning = ""
        self.inputs = {}
        self.outputs = {}
        self.confidence_score = 1.0
        self.search_service = RAGSearchService()

    def run(self, query: str) -> AgentMessageLog:
        self.status = "Searching"
        self.inputs = {"query": query}
        self.reasoning = f"Running hybrid keyword/vector search against historical tender databases."
        
        matches = self.search_service.search_historical_tenders(query)
        
        self.status = "Completed"
        self.outputs = {
            "historical_references": matches,
            "similar_cases_count": len(matches)
        }
        self.confidence_score = 0.94
        self.reasoning = (
            f"Successfully identified {len(matches)} historical tender blueprints (e.g. Smart City Analytics Portal 2024 "
            f"and Smart Irrigation Analytics Engine 2025) to utilize as proposal templates."
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
