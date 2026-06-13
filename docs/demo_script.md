# TenderPilot AI - Video Recording Guide & Demo Script

Use this script as your step-by-step recording guide. It is designed to fit under the **3-minute limit** and is optimized for the **Demo Video** hackathon requirements.

---

## 🎬 Video Recording Blueprint

### Section 1: Intro & The Problem (0:00 - 0:30)
*   **What to show on Screen (Visual)**:
    1. Open `frontend/index.html` in your browser.
    2. Start on the **Executive Dashboard** tab.
    3. Hover your cursor over the **Opportunity Radar** boxes and the **Autonomy Score** circle.
*   **Voiceover (What to Say)**:
    > "Hi everyone, welcome to TenderPilot AI, our project for the Microsoft Build AI Hackathon 2026. 
    > Businesses and startups lose thousands of dollars in opportunities simply because government tenders are scattered across fragmented portals. Finding bids, reading complex 100-page specification documents, and preparing proposals is a completely manual bottleneck. 
    > That is why we built TenderPilot AI—an autonomous team of AI agents that operates like a virtual business development assistant to find, evaluate, and draft proposals for government tenders."

---

### Section 2: Launching the Crawl (0:30 - 1:15)
*   **What to show on Screen (Visual)**:
    1. Click the **"Simulate Portal Crawl (CPPP)"** button in the top right.
    2. Immediately switch to the **Agent Workforce** tab.
    3. Watch the SVG node graph activate. The links between nodes will light up green, and the agent inspector cards below will change status.
    4. Scroll down the **Real-time Agent Timeline** as console logs start printing out.
*   **Voiceover (What to Say)**:
    > "Let's start the crawl. We search for 'AI and software development tenders under 50 Lakhs'. 
    > Immediately, our **Supervisor Agent** coordinates the workflow. The **Discovery Agent** uses Playwright to navigate the CPPP portal and download the tender specifications. 
    > Next, the **Eligibility Agent** parses the text, matches it against our profile, and calculates three key metrics: our eligibility criteria fit, our Tender Match Score which stands at 92%, and our estimated Win Probability."

---

### Section 3: RAG, Competitors & Drafting (1:15 - 2:00)
*   **What to show on Screen (Visual)**:
    1. Stay on the **Agent Workforce** tab.
    2. Watch the SVG highlight links move from the Eligibility node (EA) to the Research (RA), Competitor (CI), Planner (PA), and Generator (GA) nodes.
    3. Focus on the timeline log showing the RAG search results and previous winner insights.
*   **Voiceover (What to Say)**:
    > "Next, the **Research Agent** queries our historical files using Azure AI Search to find similar past proposals. 
    > The **Competitor Intelligence Agent** searches past award databases—identifying our competitor AlphaTech Systems, and recommending a strategic bid price of 41 Lakhs. 
    > The **Planner Agent** immediately structures a 4-step checklist, and the **Generator Agent** drafts the technical bid chapters, bringing our proposal readiness to 90%."

---

### Section 4: Human-in-the-Loop Approval Gate (2:00 - 2:30)
*   **What to show on Screen (Visual)**:
    1. Switch to the **Human Approvals** tab.
    2. Hover over the staged Outlook email draft and the staged Microsoft Planner task cards.
    3. Click on the text box, type: `"Bid price approved at 41 Lakhs."`
    4. Click the green **"Approve & Execute"** button.
*   **Voiceover (What to Say)**:
    > "For security and governance, TenderPilot uses a strict Human-in-the-Loop gate. Before any task is sent to Microsoft Planner or emails are sent via Outlook, the drafts are held here for review. 
    > We can review the pricing, leave feedback, and click 'Approve & Execute'. The Supervisor agent then publishes the tasks to our team boards using the Microsoft Graph API."

---

### Section 5: Conclusion & Tender Copilot (2:30 - 3:00)
*   **What to show on Screen (Visual)**:
    1. Switch to the **Tender Copilot** tab.
    2. Click the suggested query button: `"What documents are missing from the checklist?"`
    3. Wait 1 second for the chat bubble reply to write out, then hover over the reply.
    4. Switch back to the **Executive Dashboard** to show the updated Autonomy Score and new row in the tenders feed.
*   **Voiceover (What to Say)**:
    > "The system updates our Gremlin Knowledge Graph memory in Cosmos DB, and the dashboard updates. 
    > We can also chat with our **Tender Copilot** using natural language to explain our bidding strategy, check for missing compliance documents, or audit deadlines. 
    > TenderPilot AI turns manual procurement into a smart, autonomous experience. Thank you for watching!"

---

## 💡 Visual Recording Tips for a High Score:
1.  **Run locally or in Sandbox**: The sandbox simulator runs locally with 100% reliability, ensuring no network lags, server errors, or CAPTCHA popups disrupt your recording.
2.  **Resolution**: Make sure to record in at least **1080p** so the terminal logs and dashboard texts are sharp and readable.
3.  **No Slideshows**: The hackathon judges explicitly request a "walkthrough of the working prototype, not a slideshow". Keep your video focused entirely on the live dashboard screen.
