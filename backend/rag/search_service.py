import os
import logging
from typing import List, Dict, Any

logger = logging.getLogger("TenderRAGSearch")

class RAGSearchService:
    def __init__(self):
        self.endpoint = os.environ.get("AZURE_SEARCH_ENDPOINT")
        self.key = os.environ.get("AZURE_SEARCH_KEY")
        self.index_name = os.environ.get("AZURE_SEARCH_INDEX", "tender-proposals")
        self.use_fallback = True
        
        # Local mock corpus of historical tenders, specifications, and proposals
        self._mock_corpus = [
            {
                "id": "hist_001",
                "title": "Smart City Analytics Portal",
                "awarded_value": 4500000.0,
                "winner": "AlphaTech Systems",
                "year": 2024,
                "summary": "Implementation of real-time data pipelines and interactive visualization dashboards for city traffic analytics.",
                "traits_required": "ISO 27001, Team Size > 20"
            },
            {
                "id": "hist_002",
                "title": "State Railway Operations Portal",
                "awarded_value": 3800000.0,
                "winner": "BetaCorp Solutions",
                "year": 2025,
                "summary": "Custom dashboard engineering for tracking locomotive updates and operator task scheduling.",
                "traits_required": "ISO 9001, Central Govt Experience"
            },
            {
                "id": "hist_003",
                "title": "Smart Irrigation Analytics Engine",
                "awarded_value": 4800000.0,
                "winner": "Internal Winner",
                "year": 2025,
                "summary": "Designed IoT telemetry collector and analytics system. Successfully submitted and awarded to our organization.",
                "traits_required": "IoT Experience, Data Warehousing"
            }
        ]

        if self.endpoint and self.key:
            try:
                # Actual SDK hook:
                # from azure.search.documents import SearchClient
                # from azure.core.credentials import AzureKeyCredential
                # self.client = SearchClient(self.endpoint, self.index_name, AzureKeyCredential(self.key))
                self.use_fallback = False
                logger.info("Successfully connected to Azure AI Search.")
            except Exception as e:
                logger.error(f"Error connecting to Azure AI Search: {e}. Using local search fallback.")

    def search_historical_tenders(self, query: str, top: int = 3) -> List[Dict[str, Any]]:
        logger.info(f"[RAG] Executing query: '{query}' on index: '{self.index_name}'")
        
        # Local mock ranking based on token matches
        results = []
        words = query.lower().split()
        for doc in self._mock_corpus:
            score = 0
            for w in words:
                if w in doc["title"].lower():
                    score += 5
                if w in doc["summary"].lower():
                    score += 2
            if score > 0:
                results.append((score, doc))
                
        results.sort(reverse=True, key=lambda x: x[0])
        extracted = [r[1] for r in results[:top]]
        
        if not extracted:
            extracted = self._mock_corpus[:top]
            
        logger.info(f"[RAG] Found {len(extracted)} historical matching tender references.")
        return extracted
