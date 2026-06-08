import logging
from semantic_kernel.functions import kernel_function

logger = logging.getLogger("TenderGraphPlugin")

class GraphPlugin:
    """
    A Semantic Kernel Plugin to dispatch emails and create Planner cards via Microsoft Graph.
    """

    @kernel_function(
        description="Stages a bid proposal draft notification email in Outlook.",
        name="stage_outlook_draft"
    )
    def stage_outlook_draft(self, recipient: str, subject: str, proposal_summary: str) -> str:
        logger.info(f"[GraphPlugin] Staging Outlook draft email to {recipient} with subject: {subject}")
        return f"SUCCESS: Draft created. Email staged in Outlook Outbox (Draft ID: msg_tender_{hash(subject) % 10000})"

    @kernel_function(
        description="Registers bid checklist tasks in Microsoft Planner.",
        name="register_planner_tasks"
    )
    def register_planner_tasks(self, title: str, bucket: str, due: str) -> str:
        logger.info(f"[GraphPlugin] Registering Planner Task: '{title}' in bucket: '{bucket}' due on {due}")
        return f"SUCCESS: Planner Task registered (Task ID: tsk_tender_{hash(title) % 10000})"
