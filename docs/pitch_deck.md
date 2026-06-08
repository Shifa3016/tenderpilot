# TenderPilot AI - Pitch Deck (10 Slides Max)
**Theme**: Microsoft Build Hackathon 2026: Agentic Web  
**Tagline**: *An AI Business Development Employee that finds, evaluates, and prepares government tender opportunities autonomously.*

---

## Slide 1: Cover Page
* **Title**: TenderPilot AI  
* **Subtitle**: The Autonomous Bid & Procurement AI Workforce  
* **Tagline**: Win more business in less time.  
* **Presenter Info**: Microsoft Build 2026 Submission Team  

---

## Slide 2: The Problem (Missing Out on Bids)
* **The Complexity**: Thousands of government and PSU tenders are published daily across fragmented portals (CPPP, GeM, NHAI, smart cities, PSUs).  
* **Startup/MSME Bottleneck**: Small businesses fail to capture these opportunities because:  
  * Searching multiple portals daily is manual and error-prone.  
  * Evaluating complex 100-page eligibility PDF requirements is time-consuming.  
  * Proposal writing and checklist drafting require hundreds of man-hours.  
  * Missing a closing date results in immediate disqualification.  

---

## Slide 3: The Solution (Your Autonomous AI BD Employee)
* **Concept**: TenderPilot AI functions as an autonomous business development employee.  
* **Autonomous Web browsing**: Traverses public portals, extracts specifications, and downloads criteria files.  
* **Full Bid Preparation**: Rather than just sending alert alerts, it calculates fit, maps competitor traits, generates proposal sections, and stages project checklists.  
* **Human-in-the-Loop**: A secure control checkpoint allows BD managers to approve, edit, or reject drafts before publication.  

---

## Slide 4: Refined Multi-Agent Topology
* **8 Cooperating Agents orchestrated by Semantic Kernel**:  
  1. **Discovery Agent**: Crawls portals via Playwright to download specs.  
  2. **Eligibility Agent**: Extracts criteria and calculates eligibility fit.  
  3. **Research Agent**: Queries Azure AI Search RAG to find matching historical cases.  
  4. **Competitor Intelligence Agent**: Scrapes award history database and identifies past winners.  
  5. **Proposal Planner Agent**: Breaks requirements into task checklist roadmaps.  
  6. **Proposal Generator Agent**: Writes executive summaries and technical bid chapters.  
  7. **Execution Agent**: Stages Outlook emails and Microsoft Planner tasks.  
  8. **Reflection Agent**: Audits proposal text grounding to prevent hallucinations.  

---

## Slide 5: Strategic Decision Metrics (Three-Tier Scoring)
TenderPilot AI provides deep analytics to justify bid actions:
*   **Eligibility Score (e.g. 88%)**: Measures how many compliance prerequisites (ISO certificate, team size, location) are met.
*   **Tender Match Score™ (e.g. 92%)**: Measures budget alignment, technical capabilities, and strategic business interest.
*   **Win Probability (e.g. 76%)**: Heuristic analyzing historical win margins and competitor strength to estimate pricing success.

---

## Slide 6: The Autonomy Score™ & Opportunity Radar
* **Autonomy Score™**: A platform metric measuring how much of the procurement lifecycle runs autonomously:  
  $$\text{Autonomy Score} = \left(1 - \frac{\text{Human Interventions}}{\text{Total Actions}}\right) \times 100\%$$  
* **Opportunity Radar**: Visualizes bid priorities (High Potential, Medium Potential, Closing Soon, Requires Action) at a single glance.  

---

## Slide 7: Real-Time Demo Walkthrough
* **Scenario**: Find AI and software development tenders under ₹50 lakh.  
* **Workforce Steps**:  
  * **Crawl**: Discovery scrapes CPPP for matching bids.  
  * **Score**: Eligibility matches company size and ISO settings.  
  * **Intelligence**: Competitor Agent identifies AlphaTech and recommends an INR 41 Lakh bid price.  
  * **Planning**: Planner builds compliance checklist tasks.  
  * **Drafting**: Proposal Generator writes bid chapters.  
  * **Validation**: Reflection validates citations.  
  * **Approval**: Officer signs off via the approvals page.  

---

## Slide 8: Technical Architecture & Security
* **Data Integration**: Staged tasks are pushed directly to Exchange and Planner using the Microsoft Graph API.  
* **Identity & Governance**: Role-based access controlled by Microsoft Entra ID.  
* **Immutable Logs**: The Supervisor agent commits every prompt and human approval comment to Cosmos DB for auditing.  

---

## Slide 9: Monetization & Business Strategy
* **B2B SaaS Models**:  
  * *Standard ($2,500/mo)*: Track 5 portals, core agents.  
  * *Enterprise ($6,000/mo)*: Track 20 portals, 8 agents, custom Gremlin Graph.  
* **Market Entry**: Co-selling via Microsoft Azure Marketplace directly into O365 customers.  

---

## Slide 10: Product Roadmap
* **Phase 1 (Q3 2026)**: Core 8-agent CPPP/GeM crawls & MS Graph connectors.  
* **Phase 2 (Q1 2027)**: Gremlin Graph scaling to cross-reference multi-region bids.  
* **Phase 3 (Q3 2027)**: Self-healing templates that auto-optimize LLM prompts based on historic win/loss data.  
