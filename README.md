# TenderPilot AI: Autonomous Bid & Procurement AI Workforce

**Microsoft Build AI Hackathon 2026 Submission**  
**Category**: Agentic Web  
**Tagline**: *An AI Business Development Employee that finds, evaluates, and prepares government tender opportunities autonomously.*

---

## 🌟 Core Vision & Wow Factor

TenderPilot AI is an **Autonomous AI Business Development Employee** designed to eliminate the manual bottleneck of searching public tender portals (CPPP, GeM, NHAI), assessing eligibility, compiling checklists, researching competitors, and drafting proposals. 

Orchestrated by Semantic Kernel, the platform coordinates **8 specialized AI agents** to discover tenders, calculate fit scores, research historical awards, evaluate rival bid patterns, draft bid chapters, and stage Microsoft Office tasks—while keeping humans in control through secure governance approval checkpoints.

---

## 🛠️ Complete Microsoft Tech Stack Integration

TenderPilot AI is built from the ground up for the Microsoft ecosystem:
* **Azure OpenAI (GPT-4o)**: Powers agent reasoning, eligibility audits, and proposal drafting.
* **Semantic Kernel**: The multi-agent orchestrator managing planning, memory context, and tool calling.
* **Azure AI Search (RAG)**: Connects agents to internal proposal databases and historical bids.
* **Azure Cosmos DB**: Stores short-term session memory (NoSQL) and long-term organizational relations (Gremlin Graph API).
* **Microsoft Graph API**: Connects the Execution Agent to Outlook (Exchange) and Microsoft Planner.
* **Azure AI Foundry (Prompt Flow)**: Manages and evaluates LLM prompt templates for coherence, grounding, and validation.
* **Azure Container Apps & Functions**: Hosts backend FastAPI services and scheduled scraper runtimes.
* **Azure Monitor & App Insights**: Provides end-to-end telemetry and tokens trace tracking for agent actions.

---

## 📂 Repository Structure

```
├── backend/
│   ├── api/routes.py          # REST controllers & Tender Copilot API
│   ├── agents/                # Supervisor, Discovery, Eligibility, Research, Competitor, Planner, Generator, Execution, Reflection
│   ├── workflows/             # 13-step state orchestrator
│   ├── memory/                # Cosmos NoSQL & Knowledge Graph connectors
│   ├── rag/search_service.py  # Azure AI Search RAG wrapper
│   ├── plugins/               # Playwright browser & MS Graph SDK wrappers
│   ├── models/data_models.py  # Pydantic schemas for db collections
│   ├── tests/test_tenders.py  # Pytest automated testing suite
│   ├── main.py                # FastAPI entrypoint
│   └── requirements.txt       # Dependencies
├── frontend/
│   ├── index.html             # futuristic glassmorphism layout
│   ├── style.css              # Custom keyframe animations, grid layouts
│   └── app.js                 # SVG Collaboration Graph & 13-step demo flow
├── infra/
│   ├── main.bicep             # Azure Resource deployments Bicep templates
│   ├── prompt_flow.yaml       # Prompt Flow definitions for Azure AI Foundry
│   └── azure.yaml             # Azure Developer CLI deploy descriptors
├── docs/
│   ├── pitch_deck.md          # 10-slide Presentation Outline
│   ├── demo_script.md         # Video Script & Walkthrough
│   ├── competitive_analysis.md# Market positioning comparisons
│   ├── monetization.md        # SaaS pricing structures
│   └── roadmap.md             # Development roadmap
└── README.md                  # This file
```

---

## 🚀 Quick Start & Running Locally

### 1. Zero-Install Frontend Demo (Fastest Way to Judge)
To run the high-fidelity demonstration without setting up Python dependencies:
1. Open the [frontend/index.html](file:///e:/Projects/Microsoft%20Build%20AI/frontend/index.html) file directly in any modern web browser.
2. The UI will detect that the backend is offline and launch its **Local Sandbox Simulator**.
3. Click the **"Simulate Portal Crawl (CPPP)"** button in the header and watch the SVG Agent Collaboration Graph animate live!
4. Navigate to the **Human Approvals** tab to review staged outputs and submit governance feedback.

### 2. Full Local Development (FastAPI Backend)
To launch the backend API service:
1. Ensure Python 3.10+ is installed.
2. Clone the repository and navigate to the directory.
3. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
4. Start the FastAPI server:
   ```bash
   python backend/main.py
   ```
5. The backend will start on `http://localhost:8000`. Re-opening or refreshing the `index.html` dashboard will automatically transition it from Sandbox Mode to Live API Mode.

### 3. Running Automated Tests
To execute agent lifecycle tests:
```bash
pytest backend/tests/
```
