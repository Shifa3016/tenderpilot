// TENDERPILOT AI - FRONTEND APPLICATION SCRIPT

const BACKEND_URL = "http://localhost:8000/api";
let useLocalSimFallback = true;
let currentDemoStep = 0;
let demoInterval = null;

// System Cache data
let appMetrics = {
    autonomy_score: 91.0,
    tenders_found: 23,
    analyzed_automatically: 23,
    proposals_drafted: 7,
    opportunity_radar: {
        high_potential: 2,
        medium_potential: 5,
        closing_soon: 3,
        requires_action: 0,
        newly_discovered: 4
    }
};

// Document Load Event
document.addEventListener("DOMContentLoaded", () => {
    checkBackendConnection();
    initTabNavigation();
    initChatCopilot();
    initDemoButton();
    initApprovalActions();
    updateUIStats();
});

// Check API Service Connectivity
async function checkBackendConnection() {
    try {
        const res = await fetch(`${BACKEND_URL}/tenders`);
        if (res.ok) {
            useLocalSimFallback = false;
            console.log("[TenderPilot] Connected to live API backend. Live mode active.");
            fetchMetrics();
        }
    } catch (err) {
        console.warn("[TenderPilot] Live API backend offline. Running in local sandbox mode.");
    }
}

// Navigation Tab Swaps
function initTabNavigation() {
    const navItems = document.querySelectorAll(".nav-item");
    const panels = document.querySelectorAll(".tab-panel");
    const pageTitle = document.getElementById("page-title");
    const pageSubtitle = document.getElementById("page-subtitle");

    navItems.forEach(item => {
        item.addEventListener("click", (e) => {
            e.preventDefault();
            const tabName = item.getAttribute("data-tab");

            // Update active states
            navItems.forEach(n => n.classList.remove("active"));
            item.classList.add("active");

            panels.forEach(p => p.classList.remove("active"));
            document.getElementById(`tab-${tabName}`).classList.add("active");

            // Update headers text
            if (tabName === "dashboard") {
                pageTitle.textContent = "Executive Dashboard";
                pageSubtitle.textContent = "Real-time oversight of TenderPilot AI business development workforce.";
            } else if (tabName === "discovery-feed") {
                pageTitle.textContent = "Tender Opportunity Feed";
                pageSubtitle.textContent = "Live list of monitored feeds and discovered circular bids.";
            } else if (tabName === "agents-monitor") {
                pageTitle.textContent = "Autonomous Workforce Monitor";
                pageSubtitle.textContent = "Trace multi-agent execution paths and workflow coordination.";
            } else if (tabName === "approval-center") {
                pageTitle.textContent = "Governance Control Point";
                pageSubtitle.textContent = "Human-in-the-loop review of proposals and task checklists.";
            } else if (tabName === "copilot-center") {
                pageTitle.textContent = "Tender Copilot Command";
                pageSubtitle.textContent = "Ask queries regarding compliance checklists, competitive bidding amounts, or awards history.";
            } else if (tabName === "architecture-viz") {
                pageTitle.textContent = "Ecosystem Topology Blueprint";
                pageSubtitle.textContent = "Microsoft Azure infrastructure design mappings.";
            }
        });
    });
}

// Update UI metrics
function updateUIStats() {
    document.getElementById("autonomy-score-val").textContent = `${appMetrics.autonomy_score}%`;
    document.getElementById("kpi-autonomy").textContent = `${appMetrics.autonomy_score}%`;
    
    // Radial dashoffset logic
    const offset = 251.2 - (251.2 * appMetrics.autonomy_score) / 100;
    document.getElementById("autonomy-radial-bar").style.strokeDashoffset = offset;

    document.getElementById("kpi-tenders-found").textContent = `${appMetrics.tenders_found} Tenders`;
    document.getElementById("kpi-drafts-ready").textContent = `${appMetrics.proposals_drafted} Proposals`;
    
    document.getElementById("mini-found-val").textContent = appMetrics.tenders_found;
    document.getElementById("mini-drafts-val").textContent = appMetrics.proposals_drafted;

    // Opportunity Radar Card numbers
    document.getElementById("radar-high-val").textContent = appMetrics.opportunity_radar.high_potential;
    document.getElementById("radar-medium-val").textContent = appMetrics.opportunity_radar.medium_potential;
    document.getElementById("radar-closing-val").textContent = appMetrics.opportunity_radar.closing_soon;
    document.getElementById("radar-action-val").textContent = appMetrics.opportunity_radar.requires_action;

    const isRunning = appMetrics.opportunity_radar.requires_action > 0 || currentDemoStep > 0;
    document.getElementById("active-agents-badge").textContent = isRunning ? "Executing" : "Idle";
    document.getElementById("active-agents-badge").className = isRunning ? "badge alert-badge" : "badge";
    
    if (appMetrics.opportunity_radar.requires_action > 0) {
        document.getElementById("approval-count-badge").textContent = appMetrics.opportunity_radar.requires_action;
        document.getElementById("approval-count-badge").style.display = "inline-block";
    } else {
        document.getElementById("approval-count-badge").style.display = "none";
    }
}

// Fetch live backend metrics
async function fetchMetrics() {
    if (useLocalSimFallback) return;
    try {
        const res = await fetch(`${BACKEND_URL}/metrics`);
        if (res.ok) {
            const data = await res.json();
            appMetrics = data;
            updateUIStats();
        }
    } catch (err) {
        console.error("Error fetching metrics:", err);
    }
}

// ----------------------------------------------------
// 13-STEP DEMO SIMULATION LOOP
// ----------------------------------------------------
function initDemoButton() {
    const btn = document.getElementById("trigger-demo-btn");
    btn.addEventListener("click", () => {
        if (appMetrics.opportunity_radar.requires_action > 0) {
            alert("A bid proposal review is currently active. Please resolve it in the Approvals Center first.");
            return;
        }
        startDemoSimulation();
    });

    const triggerCrawl = document.getElementById("crawling-action-btn");
    if (triggerCrawl) {
        triggerCrawl.addEventListener("click", () => startDemoSimulation());
    }
}

function startDemoSimulation() {
    // Navigate user to Agent Monitor to watch execution flow
    document.querySelector('[data-tab="agents-monitor"]').click();

    // Reset visual components
    resetAgentGraphStyles();
    const timeline = document.getElementById("live-timeline-log");
    timeline.innerHTML = "";

    currentDemoStep = 1;
    logTimelineEvent("16:07:01 - [System Gateway] Scan triggered matching query: 'Find AI and Software Development tenders under ₹50 lakh'...", "active-event");
    highlightNode("node-supervisor");
    
    document.getElementById("agent-graph-status").textContent = "Supervisor Coordinating";
    document.getElementById("agent-graph-status").className = "badge alert-badge";

    demoInterval = setInterval(processNextDemoStep, 2000);
}

function processNextDemoStep() {
    currentDemoStep++;
    
    if (currentDemoStep === 2) {
        // Step 2: Discovery Agent scans portals
        logTimelineEvent("16:07:03 - [Supervisor] Instructing Discovery Agent to scan CPPP and GeM Portals.");
        highlightNode("node-discovery");
        highlightLink("link-sup-disc");
        updateInspectorCard("card-inspect-discovery", "Searching portals", "Crawling CPPP listings tables...", "98%");
        
    } else if (currentDemoStep === 3) {
        logTimelineEvent("16:07:06 - [Discovery Agent] Found 1 matching tender: 'Implementation of Real-time AI Operations & Big Data Analytics Dashboard' (INR 45 Lakhs).");
        logTimelineEvent("16:07:08 - [Discovery Agent] Scraped specifications PDF and downloaded local copy. Tender ID: CPPP/AI-ANALYSIS/2026/089.", "success-event");
        updateInspectorCard("card-inspect-discovery", "Done", "Saved raw specifications PDF to blob storage.", "98%");
        
    } else if (currentDemoStep === 4) {
        // Step 3 & 4: Eligibility Agent
        logTimelineEvent("16:07:10 - [Supervisor] Directing specification text to Eligibility Agent.");
        highlightNode("node-eligibility");
        highlightLink("link-disc-elig");
        updateInspectorCard("card-inspect-eligibility", "Evaluating eligibility", "Matching ISO credentials and company size limits...", "95%");
        
    } else if (currentDemoStep === 5) {
        logTimelineEvent("16:07:12 - [Eligibility Agent] Score computed: Eligibility Score (88%), Tender Match Score™ (92%), Win Probability (76%). Status: Eligible.", "success-event");
        updateInspectorCard("card-inspect-eligibility", "Done", "Tender Match: 92%. Status: Eligible.", "95%");
        
    } else if (currentDemoStep === 6) {
        // Step 5: Research Agent (RAG)
        logTimelineEvent("16:07:14 - [Supervisor] Engaging Research Agent for historical proposal examples.");
        highlightNode("node-research");
        highlightLink("link-elig-res");
        updateInspectorCard("card-inspect-research", "RAG querying", "Querying Azure AI Search past-bids catalog...", "92%");
        
    } else if (currentDemoStep === 7) {
        logTimelineEvent("16:07:16 - [Research Agent] Search completed. Retrieved 2 similar awarded bid templates: Smart City Analytics Portal 2024 and Smart Irrigation Analytics 2025.", "success-event");
        updateInspectorCard("card-inspect-research", "Done", "Retrieved 2 similar proposal templates.", "92%");
        
    } else if (currentDemoStep === 8) {
        // Step 6: Competitor Intelligence Agent
        logTimelineEvent("16:07:18 - [Supervisor] Routing to Competitor Intelligence Agent.");
        highlightNode("node-competitor");
        highlightLink("link-res-comp");
        updateInspectorCard("card-inspect-competitor", "Analyzing Rivals", "Crawling award history for AlphaTech and BetaCorp...", "93%");
        
    } else if (currentDemoStep === 9) {
        logTimelineEvent("16:07:20 - [Competitor Agent] AlphaTech identified as primary past winner. Recommendation: Set bid price to INR 41 Lakhs to match pricing patterns.", "success-event");
        updateInspectorCard("card-inspect-competitor", "Done", "AlphaTech and BetaCorp profiles analyzed.", "93%");
        
    } else if (currentDemoStep === 10) {
        // Step 7: Proposal Planner Agent
        logTimelineEvent("16:07:22 - [Supervisor] Directing outputs to Proposal Planner Agent.");
        highlightNode("node-planner");
        highlightLink("link-comp-plan");
        updateInspectorCard("card-inspect-planner", "Structuring roadmap", "Building bid checklist and roles assignments...", "95%");
        
    } else if (currentDemoStep === 11) {
        logTimelineEvent("16:07:24 - [Planner Agent] Generated bid checklist (4 tasks). Set priority: Assemble ISO 27001 document to match competitor traits.", "success-event");
        updateInspectorCard("card-inspect-planner", "Done", "Bid roadmap of 4 tasks structured.", "95%");
        
    } else if (currentDemoStep === 12) {
        // Step 8: Proposal Generator Agent
        logTimelineEvent("16:07:26 - [Supervisor] Activating Proposal Generator Agent.");
        highlightNode("node-generator");
        highlightLink("link-plan-gen");
        updateInspectorCard("card-inspect-generator", "Drafting Proposal", "Writing executive summary and compliance matrix chapters...", "94%");
        
    } else if (currentDemoStep === 13) {
        logTimelineEvent("16:07:28 - [Proposal Gen Agent] Technical proposal chapters compiled. Readiness: 90%. Staged executive summary bid draft.", "success-event");
        updateInspectorCard("card-inspect-generator", "Done", "Executive summary and technical chapters written.", "94%");
        
    } else if (currentDemoStep === 14) {
        // Step 9: Execution Agent
        logTimelineEvent("16:07:30 - [Supervisor] Instructing Execution Agent to stage Graph outputs.");
        highlightNode("node-execution");
        highlightLink("link-gen-exec");
        updateInspectorCard("card-inspect-execution", "Drafting outputs", "Staging Outlook notification emails and Planner cards...", "96%");
        
    } else if (currentDemoStep === 15) {
        logTimelineEvent("16:07:32 - [Execution Agent] Staged 1 Outlook notification email to BD-team and 4 compliance tasks in staging cache.", "success-event");
        updateInspectorCard("card-inspect-execution", "Done (Staged)", "Awaiting Governance clearance.", "96%");
        
    } else if (currentDemoStep === 16) {
        // Step 10: Reflection Agent
        logTimelineEvent("16:07:34 - [Supervisor] Triggering Reflection Agent for citation grounding checks.");
        highlightNode("node-reflection");
        highlightLink("link-exec-ref");
        updateInspectorCard("card-inspect-reflection", "Auditing bid files", "Checking document checklist deadlines...", "97%");
        
    } else if (currentDemoStep === 17) {
        logTimelineEvent("16:07:36 - [Reflection Agent] Citation check: PASS. Hallucination risk: <1%. Proposal draft certified with 95% confidence score.", "success-event");
        updateInspectorCard("card-inspect-reflection", "Done", "Citations grounded. Deadline checkpoints validated.", "97%");
        
        // Pause demo loop and open governance approvals modal
        clearInterval(demoInterval);
        triggerGovernanceApprovalScreen();
    }
}

// Open human approval checkpoint modal
function triggerGovernanceApprovalScreen() {
    logTimelineEvent("16:07:38 - [Supervisor] Paused workflow. Governance checkpoint active. Awaiting review signature.", "active-event");
    
    document.getElementById("agent-graph-status").textContent = "Awaiting Approval";
    document.getElementById("agent-graph-status").className = "badge alert-badge";

    // Update Opportunity Radar requires action count
    appMetrics.opportunity_radar.requires_action = 1;
    updateUIStats();

    // Fill staged email draft
    document.getElementById("mock-email-subject").textContent = "Action Required: Proposal Roadmap staged for 'Implementation of Real-time AI Operations & Big Data Analytics Dashboard'";
    document.getElementById("mock-email-body").textContent = 
        "Hi Team,\n\n" +
        "Our autonomous agent has analyzed 'Implementation of Real-time AI Operations & Big Data Analytics Dashboard' (Tender ID: CPPP/AI-ANALYSIS/2026/089) " +
        "and calculated a 92% Tender Match Score. We have staged a proposal draft.\n\n" +
        "The following bid tasks have been structured on Microsoft Planner:\n" +
        "- Assemble ISO 27001 Certification PDF (Assignee: Compliance lead, Due: 2026-06-15)\n" +
        "- Compile Case Study of Smart Irrigation project (Assignee: Engineering Director, Due: 2026-06-18)\n" +
        "- Draft Financial Bid Worksheet (Assignee: Finance Controller, Due: 2026-06-22)\n" +
        "- Consolidate Technical Architecture Writeup (Assignee: Principal Architect, Due: 2026-06-24)\n\n" +
        "Please review the bid drafts and approve execution on the TenderPilot dashboard.\n\n" +
        "Regards,\nTenderPilot AI Workforce";

    // Populate Tasks list
    const tasksDiv = document.getElementById("mock-staged-tasks");
    tasksDiv.innerHTML = `
        <div class="planner-task-card">
            <h5>1. Assemble ISO 27001 Certification PDF</h5>
            <p>Retrieve active ISO certificate from IT Security vaults.</p>
            <span>Role: Compliance lead | Due: June 15, 2026</span>
        </div>
        <div class="planner-task-card">
            <h5>2. Compile Case Study of Smart Irrigation project</h5>
            <p>Format historical smart irrigation metrics as past performance proof.</p>
            <span>Role: Engineering Director | Due: June 18, 2026</span>
        </div>
        <div class="planner-task-card">
            <h5>3. Draft Financial Bid Worksheet</h5>
            <p>Compile project cost matrices. Pricing set to INR 41 Lakhs.</p>
            <span>Role: Finance Controller | Due: June 22, 2026</span>
        </div>
        <div class="planner-task-card">
            <h5>4. Consolidate Technical Architecture Writeup</h5>
            <p>Review systems topology and data pipelines description.</p>
            <span>Role: Principal Architect | Due: June 24, 2026</span>
        </div>
    `;

    // Swap displays
    document.getElementById("approvals-empty-state").style.display = "none";
    document.getElementById("active-approval-card").style.display = "block";

    // Direct user to approvals center tab
    document.querySelector('[data-tab="approval-center"]').click();
}

function initApprovalActions() {
    const approveBtn = document.getElementById("btn-approval-approve");
    const modifyBtn = document.getElementById("btn-approval-modify");
    const rejectBtn = document.getElementById("btn-approval-reject");

    approveBtn.addEventListener("click", () => completeDemoWorkflow("approve"));
    modifyBtn.addEventListener("click", () => completeDemoWorkflow("modify"));
    rejectBtn.addEventListener("click", () => completeDemoWorkflow("reject"));
}

function completeDemoWorkflow(action) {
    const feedback = document.getElementById("approval-feedback-input").value;
    
    // Switch back to agent workspace tab to watch conclusion
    document.querySelector('[data-tab="agents-monitor"]').click();

    // Reset approval drawer
    document.getElementById("active-approval-card").style.display = "none";
    document.getElementById("approvals-empty-state").style.display = "flex";
    appMetrics.opportunity_radar.requires_action = 0;
    
    if (action === "approve" || action === "modify") {
        logTimelineEvent(`16:08:02 - [Human-in-the-Loop] Action approved. Review note: '${feedback || "Bidding price approved at INR 41 Lakhs."}'`, "success-event");
        
        // Execute graph creations
        highlightNode("node-supervisor");
        highlightLink("link-ref-sup");
        logTimelineEvent("16:08:04 - [Supervisor] Instructing Execution Agent to post staged Outlook draft and register Planner cards.");
        logTimelineEvent("16:08:06 - [Execution Agent] Microsoft Graph API request sent: Outlook draft created (Draft ID: msg_tender_8910).", "success-event");
        logTimelineEvent("16:08:08 - [Execution Agent] Microsoft Planner tasks registered for Compliance, Engineering, and Finance boards.", "success-event");
        
        // Knowledge Graph Updates
        highlightNode("node-supervisor");
        logTimelineEvent("16:08:10 - [Supervisor] Updating Persistent Knowledge Graph Memory. Adding vertices: Tender (Real-time AI operations dashboard), Competitors (AlphaTech Systems).");
        logTimelineEvent("16:08:12 - [Memory Layer] Knowledge Graph successfully linked nodes: Tender --(COMPETES_WITH)--> AlphaTech Systems; Task --(RESOLVES)--> Tender.", "success-event");
        
        // Complete
        logTimelineEvent("16:08:15 - [Supervisor] Workflow run successfully concluded.", "success-event");
        document.getElementById("agent-graph-status").textContent = "Workforce Completed";
        document.getElementById("agent-graph-status").className = "badge";
        
        // Add row to discovery feed table
        const rowHTML = `
            <tr>
                <td>2026-06-08</td>
                <td>CPPP</td>
                <td><strong>Implementation of Real-time AI Operations & Big Data Analytics Dashboard</strong></td>
                <td><span class="risk-pill pill-high">92% Match</span></td>
                <td><span class="risk-pill pill-medium">88% Eligible</span></td>
                <td><span class="risk-pill pill-medium">76% Win Prob</span></td>
                <td><span class="status-badge status-completed">Completed</span></td>
            </tr>
        `;
        document.getElementById("tender-feed-rows").insertAdjacentHTML("afterbegin", rowHTML);

        // Update stats metrics
        appMetrics.autonomy_score = action === "approve" ? 92.0 : 85.0;
        appMetrics.tenders_found += 1;
        appMetrics.analyzed_automatically += 1;
        appMetrics.proposals_drafted += 1;
        
        // Update radar
        appMetrics.opportunity_radar.high_potential += 1;
        
    } else {
        logTimelineEvent(`16:08:02 - [Human-in-the-Loop] Action rejected. Reason: '${feedback || "Bid dismissed by review officer."}'`, "active-event");
        logTimelineEvent("16:08:04 - [Supervisor] Aborting workflow. Bids drafts deleted from staging cache.", "active-event");
        document.getElementById("agent-graph-status").textContent = "Workforce Aborted";
        document.getElementById("agent-graph-status").className = "badge alert-badge";
        
        appMetrics.autonomy_score = 50.0;
    }

    currentDemoStep = 0;
    updateUIStats();
    resetAgentGraphStyles();
}

// ----------------------------------------------------
// UI HELPERS
// ----------------------------------------------------
function highlightNode(nodeId) {
    document.querySelectorAll(".graph-node").forEach(n => n.classList.remove("active-node"));
    document.getElementById(nodeId).classList.add("active-node");
}

function highlightLink(linkId) {
    document.querySelectorAll(".graph-link").forEach(l => l.classList.remove("active-link"));
    document.getElementById(linkId).classList.add("active-link");
}

function resetAgentGraphStyles() {
    document.querySelectorAll(".graph-node").forEach(n => n.classList.remove("active-node"));
    document.querySelectorAll(".graph-link").forEach(l => l.classList.remove("active-link"));
}

function logTimelineEvent(text, cssClass = "") {
    const timeline = document.getElementById("live-timeline-log");
    
    if (timeline.querySelector(".timeline-empty-state")) {
        timeline.innerHTML = "";
    }
    
    const div = document.createElement("div");
    div.className = `timeline-event ${cssClass}`;
    div.textContent = text;
    timeline.appendChild(div);
    
    timeline.scrollTop = timeline.scrollHeight;
}

function updateInspectorCard(cardId, status, reasoning, confidence) {
    const card = document.getElementById(cardId);
    card.classList.add("running-agent");
    
    if (status === "Done" || status.includes("Done")) {
        card.classList.remove("running-agent");
    }

    const rows = card.querySelectorAll(".meta-row .val");
    rows[0].textContent = status;
    
    if (status === "Done" || status.includes("Done")) {
        rows[0].className = "val status-done";
    } else {
        rows[0].className = "val status-running";
    }
    
    rows[1].textContent = reasoning;
    if (rows[2]) rows[2].textContent = confidence;
}

// ----------------------------------------------------
// TENDER COPILOT CONVERSATIONAL CHAT
// ----------------------------------------------------
function initChatCopilot() {
    const input = document.getElementById("copilot-chat-input");
    const sendBtn = document.getElementById("copilot-send-btn");
    
    sendBtn.addEventListener("click", () => triggerChatRequest(input.value));
    input.addEventListener("keypress", (e) => {
        if (e.key === "Enter") triggerChatRequest(input.value);
    });

    const suggestions = document.querySelectorAll(".query-suggest-item");
    suggestions.forEach(item => {
        item.addEventListener("click", () => triggerChatRequest(item.textContent));
    });
}

async function triggerChatRequest(msgText) {
    if (!msgText.trim()) return;

    const chatLog = document.getElementById("copilot-chat-log");
    document.getElementById("copilot-chat-input").value = "";

    // Append user message
    const userBubble = document.createElement("div");
    userBubble.className = "chat-bubble user";
    userBubble.innerHTML = `<p>${msgText}</p>`;
    chatLog.appendChild(userBubble);
    chatLog.scrollTop = chatLog.scrollHeight;

    // Loading / thinking bubble
    const typingBubble = document.createElement("div");
    typingBubble.className = "chat-bubble bot typing";
    typingBubble.innerHTML = `<p>Thinking...</p>`;
    chatLog.appendChild(typingBubble);
    chatLog.scrollTop = chatLog.scrollHeight;

    if (!useLocalSimFallback) {
        try {
            const res = await fetch(`${BACKEND_URL}/chat`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: msgText })
            });
            if (res.ok) {
                const data = await res.json();
                typingBubble.remove();
                appendBotReply(data.reply);
                return;
            }
        } catch (err) {
            console.error("FastAPI Chat Error, switching to mock response.");
        }
    }

    // Local sandbox fallback response logic
    setTimeout(() => {
        typingBubble.remove();
        const msg = msgText.toLowerCase();
        let reply = "";

        if (msg.includes("find") || msg.includes("search") || msg.includes("tenders")) {
            reply = 
                "### Discovered Tender Opportunities\n\n" +
                "I identified **1 matching opportunity** under ₹50 lakh on CPPP:\n\n" +
                "- **Implementation of Real-time AI Operations & Big Data Analytics Dashboard**\n" +
                "  *Match Score*: **92% Match** | *Win Probability*: **76%**\n" +
                "  *Tender ID*: CPPP/AI-ANALYSIS/2026/089 | *Budget*: INR 45 Lakhs.\n" +
                "  *Closing Date*: June 30, 2026.";
        } else if (msg.includes("why") || msg.includes("potential") || msg.includes("score")) {
            reply = 
                "The CPPP smart city dashboard tender has a high **92% Tender Match Score™** due to several parameters:\n\n" +
                "1. **Budget Alignment**: The project budget is INR 45 Lakhs, which fits within our target sweet spot (under 50 Lakhs).\n" +
                "2. **Technical Fit**: The requirements specify software development, dashboard telemetry interfaces, and data pipelines, matching our core competencies.\n" +
                "3. **Compliance alignment**: We meet the ISO 27001 certification and corporate existence criteria.";
        } else if (msg.includes("missing") || msg.includes("documents") || msg.includes("checklist")) {
            reply = 
                "### Staged Compliance Documents Audit\n\n" +
                "- **ISO 27001 Certification PDF**: **Present** in attachments.\n" +
                "- **IT Security Audit Certificate**: **Missing** from folder. (I have staged a Planner task for the compliance lead to retrieve it).\n" +
                "- **Technical Architecture Writeup**: **Drafted** (90% readiness).\n" +
                "- **Pricing Sheet**: **Staged** (Benchmark bid price set to INR 41 Lakhs).";
        } else if (msg.includes("close") || msg.includes("closing") || msg.includes("week")) {
            reply = 
                "### Closing Soon (Within 30 Days)\n\n" +
                "- **Real-time AI Operations & Big Data Analytics Dashboard** (CPPP/AI-ANALYSIS/2026/089)\n" +
                "  *Close Date*: June 30, 2026.\n" +
                "- **Smart Municipal Data Telemetry Dashboard** (GeM/TRAFFIC-OPS/2026)\n" +
                "  *Close Date*: July 15, 2026.";
        } else if (msg.includes("strategy") || msg.includes("bid") || msg.includes("proposal")) {
            reply = 
                "### Bid Submission Strategy Recommendations\n\n" +
                "Based on the Competitor Intelligence Agent's analysis of AlphaTech Systems (past smart city contract winner):\n\n" +
                "1. **Pricing Heuristic**: AlphaTech bids on the higher margin spectrum. I recommend a bid price of **INR 41 Lakhs** to undercut their average by 3% while retaining a 22% profit margin.\n" +
                "2. **Compliance Focus**: Highlight our active ISO 27001 certification on page 2. AlphaTech won past contracts primarily on security credentials.\n" +
                "3. **Technical Grounding**: Ground the proposal using our Smart Irrigation case study as proof of IoT telemetry performance.";
        } else {
            reply = 
                "I am your Tender Copilot. I can query active opportunity tables, check document lists, and draft strategies.\n\n" +
                "Try asking me:\n" +
                "- *'Find AI tenders under ₹50 lakh.'*\n" +
                "- *'Why was the smart city tender marked as high potential?'*\n" +
                "- *'What documents are missing from the checklist?'*\n" +
                "- *'Generate a bid submission strategy.'*";
        }

        appendBotReply(reply);
    }, 1200);
}

function appendBotReply(replyText) {
    const chatLog = document.getElementById("copilot-chat-log");
    const botBubble = document.createElement("div");
    botBubble.className = "chat-bubble bot";
    
    let formattedText = replyText
        .replace(/### (.*)/g, '<h3>$1</h3>')
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        .replace(/\n\n/g, '<br><br>')
        .replace(/- (.*)/g, '<li>$1</li>');
        
    botBubble.innerHTML = formattedText;
    chatLog.appendChild(botBubble);
    chatLog.scrollTop = chatLog.scrollHeight;
}
