# TenderPilot AI - 3-Minute Demo Video Script & Narrative

This document details the video storyboard, voiceover lines, and judges walkthrough instructions for the TenderPilot AI hackathon submission.

---

## 3-Minute Video Storyboard

| Timestamp | Visual Layout | Spoken Voiceover |
| :--- | :--- | :--- |
| **0:00 - 0:25** | Host appears. Screenshare showing the **Executive Dashboard**. The dashboard has clean glassmorphic panels and a glowing radial **Autonomy Score™** progress bar reading 91%. | "Every day, thousands of government tenders are published across fragmented portals. Startups and MSMEs miss these opportunities because tracking them, evaluating eligibility, and preparing proposals is a manual bottleneck. Meet TenderPilot AI—an autonomous AI Business Development Employee that finds, evaluates, and prepares bids autonomously." |
| **0:25 - 1:10** | Zoom in on the **Agent Workforce** panel. The user clicks **'Simulate Portal Crawl'**. The live SVG **Agent Collaboration Graph** lights up. Green links start pulsing between the Supervisor, Discovery, and Eligibility nodes. Terminal logs stream in real-time. | "Let's trigger a portal crawl. The Discovery Agent navigates CPPP, downloading a new Smart City dashboard tender. The **Eligibility Agent** parses the specifications PDF against our company credentials. It calculates three key metrics: a 92% Match Score, an 88% Eligibility Score, and a 76% Win Probability." |
| **1:10 - 1:50** | The collaboration graph pulses toward the **Research Agent**, then the **Competitor Intelligence**, **Planner**, and **Generator** nodes. The timeline prints details about RAG matches, previous winners (AlphaTech Systems), and technical draft chapters. | "Next, the **Research Agent** queries Azure AI Search for past bids. The **Competitor Intelligence Agent** analyzes past winner patterns, identifying AlphaTech Systems as the primary rival and recommending a strategic bid price of INR 41 Lakhs. The **Planner** designs a task checklist, and the **Generator Agent** drafts proposal chapters." |
| **1:50 - 2:30** | Switch to the **Governance Approvals** page. An approval card is displayed. The host inspects the staged Outlook email draft and the four Microsoft Planner cards. Host types feedback: "Approved for deployment" and clicks **'Approve & Execute'**. | "TenderPilot AI keeps humans in control. Staged tasks and proposals are held at this **Human-in-the-Loop Governance Checkpoint**. Here, we can review the drafts and pricing. Clicking approve triggers the Supervisor agent to dispatch the tasks and emails using the Microsoft Graph API." |
| **2:30 - 3:00** | Switch back to the Executive Dashboard. Show the Autonomy Score updating to 92%. Show the new row added to the **Tenders Feed** table. Open the **Tender Copilot** chat, ask a suggested query, and show the instant response. | "On completion, the system updates our persistent Gremlin Knowledge Graph in Cosmos DB, and the dashboard metrics refresh. We can query our database using the **Tender Copilot**. Businesses no longer need to waste hours hunting for tenders. TenderPilot AI does the work for you." |

---

## Judges Presentation Narrative

### The Core Theme: Agentic Web
TenderPilot AI demonstrates the "Agentic Web" by giving AI agents web autonomy. Rather than relying on static APIs, our workforce uses Playwright browser agents to traverse portals, authenticate, extract updates, map dependencies, and write actions directly back into Microsoft SaaS networks.

### Walkthrough Steps for Evaluators
To follow the simulation on the live frontend:
1. Navigate to the **Autonomous Workforce** tab to inspect the interactive collaboration graph.
2. Click the **'Simulate Portal Crawl (CPPP)'** button in the header.
3. Watch the SVG graph highlight the active agent node in real-time, accompanied by live console logs in the timeline.
4. Go to the **Human Approvals** tab once the Reflection Agent validation completes.
5. Review the staged email copy and the 4 Microsoft Planner tasks.
6. Provide custom feedback in the input box and click **'Approve & Execute'**.
7. Return to the **Executive Dashboard** to verify that the metrics, autonomy score, and feed tables have updated dynamically.
8. Ask custom questions (e.g., *"Show all high-risk regulatory updates this month."*) in the **Executive Copilot** chat interface.
