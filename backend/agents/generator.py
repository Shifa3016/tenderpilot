import logging
from typing import Dict, Any, List
from datetime import datetime
from backend.models.data_models import AgentMessageLog, ProposalDraft, ProposalSection

logger = logging.getLogger("ProposalGenerator")

class ProposalGeneratorAgent:
    def __init__(self):
        self.name = "Proposal Generator Agent"
        self.goal = "Draft high-quality executive summaries, technical bid proposal writeups, and compliance mapping lists."
        self.status = "Idle"
        self.reasoning = ""
        self.inputs = {}
        self.outputs = {}
        self.confidence_score = 1.0

    def run(self, tender_title: str, requirements: List[str]) -> AgentMessageLog:
        self.status = "Drafting Proposal"
        self.inputs = {
            "tender_title": tender_title,
            "requirements": requirements
        }
        self.reasoning = "Formulating executive pitch and technical response sections grounded in historical winning cases."
        
        # 1. Executive Summary
        exec_summary = (
            f"EXECUTIVE BID SUMMARY FOR: {tender_title}\n\n"
            f"TenderCorp Technologies is pleased to submit this proposal for the '{tender_title}'. "
            f"Leveraging our proven experience in Smart analytics architectures, we deliver a scalable "
            f"data operations dashboard supporting real-time telemetry analytics. Our proposed solution "
            f"incorporates node clustering, role-based access controls, and cold logs backup isolation, "
            f"ensuring 100% compliance with government security frameworks."
        )
        
        # 2. Technical Sections
        tech_sections = [
            ProposalSection(
                section_title="1. Technical Architecture & Data Ingestion",
                content=(
                    "The system architecture is engineered using event-driven microservices. "
                    "Data ingestion is handled via Azure Event Grid and Service Bus queues to support "
                    "seamless scaling under high traffic telemetry loads. Dashboards display real-time "
                    "analytics metrics with an sub-second rendering latency."
                ),
                word_count=350
            ),
            ProposalSection(
                section_title="2. Cybersecurity Controls & Compliance Matrix",
                content=(
                    "In alignment with strict regulatory guidelines, our deployment enforces: "
                    "1. Multi-Factor Authentication (MFA) via Entra ID integration. "
                    "2. Read-only log isolation storage to mitigate audit tampering risks. "
                    "3. ISO 27001 governed infrastructure policies."
                ),
                word_count=220
            )
        ]
        
        # 3. Compliance checklist
        compliance_check = [
            {"clause": "ISO 27001 Certified", "response": "Yes, Certificate active, see Attachment B"},
            {"clause": "Indian Registered Entity", "response": "Yes, PAN/TIN details attached, page 4"},
            {"clause": "Previous Experience > 30L", "response": "Yes, Smart Irrigation contract details, page 12"}
        ]
        
        draft = ProposalDraft(
            tender_id="CPPP/AI-ANALYSIS/2026/089",
            executive_summary=exec_summary,
            technical_sections=tech_sections,
            compliance_checklist=compliance_check,
            readiness_percentage=90.0
        )
        
        self.status = "Completed"
        self.outputs = {
            "proposal_draft": draft.model_dump(),
            "readiness": draft.readiness_percentage
        }
        self.confidence_score = 0.94
        self.reasoning = (
            f"Drafted Executive Summary and 2 major technical proposal chapters. "
            f"Completed compliance mapping list with 90% draft readiness score."
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
