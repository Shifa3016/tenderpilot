from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

class CompetitorProfile(BaseModel):
    name: str
    award_count: int
    avg_bid_amount: float
    common_traits: List[str] = Field(default_factory=list)

class ComplianceTask(BaseModel):
    task_id: str
    title: str
    description: str
    assigned_role: str
    deadline: str
    status: str = "Staged"  # Staged, Approved, InProgress, Completed

class ProposalSection(BaseModel):
    section_title: str
    content: str
    word_count: int
    last_updated: datetime = Field(default_factory=datetime.utcnow)

class ProposalDraft(BaseModel):
    tender_id: str
    executive_summary: str = ""
    technical_sections: List[ProposalSection] = Field(default_factory=list)
    compliance_checklist: List[Dict[str, Any]] = Field(default_factory=list)
    readiness_percentage: float = 0.0

class TenderAlert(BaseModel):
    id: str
    title: str
    portal: str  # GeM, CPPP, NHAI
    budget: float  # e.g., 3500000.0 (under 50 lakh)
    publish_date: str
    close_date: str
    scraped_text: str
    
    # AI Score Metrics
    eligibility_score: float = 0.0  # 0 to 100
    tender_match_score: float = 0.0 # 0 to 100
    win_probability: float = 0.0     # 0 to 100
    eligibility_status: str = "Evaluating" # Eligible, Partially Eligible, Not Eligible
    
    # Research & Competitor Intell Outputs
    historical_citations: List[Dict[str, Any]] = Field(default_factory=list)
    previous_winners: List[CompetitorProfile] = Field(default_factory=list)
    
    # Generated Actions
    proposal: Optional[ProposalDraft] = None
    roadmap: List[ComplianceTask] = Field(default_factory=list)
    status: str = "Discovered" # Discovered, Evaluated, Staged, Completed, Rejected

class HumanApprovalItem(BaseModel):
    approval_id: str
    tender_id: str
    staged_email: Dict[str, Any] = Field(default_factory=dict)
    staged_tasks: List[Dict[str, Any]] = Field(default_factory=list)
    staged_proposal: Dict[str, Any] = Field(default_factory=dict)
    status: str = "Pending"  # Pending, Approved, Modified, Rejected
    reviewed_at: Optional[datetime] = None
    reviewer_comments: Optional[str] = None

class AgentMessageLog(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    agent_name: str
    goal: str
    status: str
    reasoning: str
    inputs: Dict[str, Any] = Field(default_factory=dict)
    outputs: Dict[str, Any] = Field(default_factory=dict)
    confidence_score: float

class WorkflowState(BaseModel):
    workflow_id: str
    tender_id: str
    current_step: int = 1
    total_steps: int = 13
    status: str = "Running"  # Running, AwaitingApproval, Completed, Failed
    logs: List[AgentMessageLog] = Field(default_factory=list)
    autonomy_score: float = 100.0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
