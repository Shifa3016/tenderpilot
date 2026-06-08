import os
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
from azure.cosmos import CosmosClient
from backend.models.data_models import TenderAlert, WorkflowState, HumanApprovalItem

logger = logging.getLogger("TenderCosmosStore")

class CosmosStore:
    def __init__(self):
        self.endpoint = os.environ.get("COSMOS_DB_ENDPOINT")
        self.key = os.environ.get("COSMOS_DB_KEY")
        self.database_name = os.environ.get("COSMOS_DB_DATABASE", "TenderPilotDB")
        self.client = None
        self.db = None
        self.use_local_memory = True
        
        # Local in-memory mock database
        self._tenders: Dict[str, Dict[str, Any]] = {}
        self._workflows: Dict[str, Dict[str, Any]] = {}
        self._approvals: Dict[str, Dict[str, Any]] = {}

        if self.endpoint and self.key:
            try:
                self.client = CosmosClient(self.endpoint, self.key)
                self.db = self.client.get_database_client(self.database_name)
                self.use_local_memory = False
                logger.info("Successfully connected to Azure Cosmos DB.")
            except Exception as e:
                logger.error(f"Error connecting to Azure Cosmos DB: {e}. Using local in-memory fallback.")

    def save_tender(self, tender: TenderAlert):
        if self.use_local_memory:
            self._tenders[tender.id] = tender.model_dump()
            return
        try:
            container = self.db.get_container_client("Tenders")
            container.upsert_item(tender.model_dump())
        except Exception as e:
            logger.error(f"Cosmos write error: {e}")
            self._tenders[tender.id] = tender.model_dump()

    def get_tender(self, tender_id: str) -> Optional[TenderAlert]:
        if self.use_local_memory:
            data = self._tenders.get(tender_id)
            return TenderAlert(**data) if data else None
        try:
            container = self.db.get_container_client("Tenders")
            data = container.read_item(item=tender_id, partition_key=tender_id)
            return TenderAlert(**data)
        except Exception:
            data = self._tenders.get(tender_id)
            return TenderAlert(**data) if data else None

    def get_all_tenders(self) -> List[TenderAlert]:
        if self.use_local_memory:
            return [TenderAlert(**v) for v in self._tenders.values()]
        try:
            container = self.db.get_container_client("Tenders")
            items = list(container.read_all_items())
            return [TenderAlert(**item) for item in items]
        except Exception:
            return [TenderAlert(**v) for v in self._tenders.values()]

    def save_workflow(self, workflow: WorkflowState):
        workflow.updated_at = datetime.utcnow()
        if self.use_local_memory:
            self._workflows[workflow.workflow_id] = workflow.model_dump()
            return
        try:
            container = self.db.get_container_client("Workflows")
            container.upsert_item(workflow.model_dump())
        except Exception as e:
            logger.error(f"Cosmos write error: {e}")
            self._workflows[workflow.workflow_id] = workflow.model_dump()

    def get_workflow(self, workflow_id: str) -> Optional[WorkflowState]:
        if self.use_local_memory:
            data = self._workflows.get(workflow_id)
            return WorkflowState(**data) if data else None
        try:
            container = self.db.get_container_client("Workflows")
            data = container.read_item(item=workflow_id, partition_key=workflow_id)
            return WorkflowState(**data)
        except Exception:
            data = self._workflows.get(workflow_id)
            return WorkflowState(**data) if data else None

    def get_all_workflows(self) -> List[WorkflowState]:
        if self.use_local_memory:
            return [WorkflowState(**v) for v in self._workflows.values()]
        try:
            container = self.db.get_container_client("Workflows")
            items = list(container.read_all_items())
            return [WorkflowState(**item) for item in items]
        except Exception:
            return [WorkflowState(**v) for v in self._workflows.values()]

    def save_approval(self, approval: HumanApprovalItem):
        if self.use_local_memory:
            self._approvals[approval.approval_id] = approval.model_dump()
            return
        try:
            container = self.db.get_container_client("Approvals")
            container.upsert_item(approval.model_dump())
        except Exception as e:
            logger.error(f"Cosmos write error: {e}")
            self._approvals[approval.approval_id] = approval.model_dump()

    def get_approval(self, approval_id: str) -> Optional[HumanApprovalItem]:
        if self.use_local_memory:
            data = self._approvals.get(approval_id)
            return HumanApprovalItem(**data) if data else None
        try:
            container = self.db.get_container_client("Approvals")
            data = container.read_item(item=approval_id, partition_key=approval_id)
            return HumanApprovalItem(**data)
        except Exception:
            data = self._approvals.get(approval_id)
            return HumanApprovalItem(**data) if data else None
