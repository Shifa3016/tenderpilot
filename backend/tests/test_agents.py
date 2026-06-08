import pytest
from backend.memory.cosmos_store import CosmosStore
from backend.memory.graph_store import GraphStore
from backend.workflows.orchestrator import WorkflowOrchestrator
from backend.models.data_models import WorkflowState, RegulatoryAlert

def test_workflow_execution_lifecycle():
    db = CosmosStore()
    graph = GraphStore()
    orchestrator = WorkflowOrchestrator(db, graph)
    
    # Trigger pipeline
    portal_url = "https://www.rbi.org.in/notifications"
    state = orchestrator.start_pipeline(portal_url)
    
    # Verify starting states
    assert state.workflow_id is not None
    assert state.status == "AwaitingApproval"
    assert state.current_step == 10  # Awaiting human input
    assert len(state.logs) == 9       # Initial trigger + 8 steps of routing & work
    
    # Verify that a regulatory alert item was stored
    alert = db.get_alert(state.alert_id)
    assert alert is not None
    assert alert.risk_score == 88.0  # High risk due to cyber keywords
    assert "dept_it" in alert.affected_departments
    assert len(alert.compliance_roadmap) == 4
    
    # Process Human Approval Action
    completed_state = orchestrator.complete_pipeline(state.workflow_id, "approve", "Approved by CISO")
    
    # Verify completion states
    assert completed_state.status == "Completed"
    assert completed_state.current_step == 13
    assert completed_state.autonomy_score == 92.0
    
    # Verify Knowledge Graph updates
    graph_data = graph.query_graph_structure()
    nodes = [n["id"] for n in graph_data["nodes"]]
    assert alert.id in nodes
    assert "task_001" in nodes
    
    # Verify edge creations
    edges = [(e["source"], e["target"], e["label"]) for e in graph_data["links"]]
    assert (alert.id, "org_rbi", "ISSUED_BY") in edges
    assert ("task_001", alert.id, "RESOLVES") in edges
