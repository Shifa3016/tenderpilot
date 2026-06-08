import pytest
from backend.memory.cosmos_store import CosmosStore
from backend.memory.graph_store import GraphStore
from backend.workflows.orchestrator import WorkflowOrchestrator
from backend.models.data_models import WorkflowState, TenderAlert

def test_tender_workflow_lifecycle():
    db = CosmosStore()
    graph = GraphStore()
    orchestrator = WorkflowOrchestrator(db, graph)
    
    # 1. Start pipeline matching user search parameters
    state = orchestrator.start_pipeline("https://cppp.gov.in", "AI Analytics dashboard under 50 lakh")
    
    # 2. Check intermediate routing states
    assert state.workflow_id is not None
    assert state.status == "AwaitingApproval"
    assert state.current_step == 11
    assert len(state.logs) == 11  # System trigger + 10 steps of agent logs
    
    # 3. Retrieve computed score matrices from memory
    tender = db.get_tender(state.tender_id)
    assert tender is not None
    assert tender.eligibility_score == 88.0
    assert tender.tender_match_score == 92.0
    assert tender.win_probability == 76.0
    assert tender.eligibility_status == "Eligible"
    assert len(tender.roadmap) == 4
    assert tender.proposal.readiness_percentage == 90.0
    
    # 4. Process human approval event
    completed_state = orchestrator.complete_pipeline(state.workflow_id, "approve", "Checked by CEO. Submit bid.")
    
    # 5. Check completed states
    assert completed_state.status == "Completed"
    assert completed_state.current_step == 13
    assert completed_state.autonomy_score == 91.0
    
    # 6. Verify knowledge graph entities insertions
    graph_data = graph.query_graph_structure()
    nodes = [n["id"] for n in graph_data["nodes"]]
    assert tender.id in nodes
    assert "tsk_001" in nodes
    
    # 7. Check graph relationship edges mapping
    edges = [(e["source"], e["target"], e["label"]) for e in graph_data["links"]]
    assert (tender.id, "portal_cppp", "SIBLING_OF") in edges
    assert ("tsk_001", tender.id, "RESOLVES") in edges
