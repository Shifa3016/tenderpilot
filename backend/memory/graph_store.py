import logging
from typing import List, Dict, Any, Optional

logger = logging.getLogger("TenderGraphStore")

class GraphStore:
    def __init__(self):
        # In-memory graph nodes and edges representation
        self.vertices: Dict[str, Dict[str, Any]] = {}
        self.edges: List[Dict[str, Any]] = []
        self._initialize_bootstrap_graph()

    def _initialize_bootstrap_graph(self):
        # 1. Internal Corporate Departments
        departments = [
            ("dept_sales", "Business Development", "Drives sales pipelines, bidding strategy, and partnerships."),
            ("dept_engineering", "Engineering Group", "Technical execution, systems design, and product engineering."),
            ("dept_legal", "Legal & Compliance", "Checks liability clauses, eligibility details, and signs terms.")
        ]
        for dept_id, name, desc in departments:
            self.add_node(dept_id, "Department", name, {"description": desc})

        # 2. Competitors / Previous Winners
        competitors = [
            ("comp_alpha", "AlphaTech Systems", {"size": "Large", "award_count": 8, "common_traits": "ISO 27001 Certified, Govt Experience"}),
            ("comp_beta", "BetaCorp Solutions", {"size": "Medium", "award_count": 5, "common_traits": "ISO 9001 Certified, Regional Focus"})
        ]
        for comp_id, name, props in competitors:
            self.add_node(comp_id, "Competitor", name, props)

        # 3. Monitored Tenders Portals
        portals = [
            ("portal_gem", "Government e-Marketplace (GeM)", {"jurisdiction": "Central India", "type": "Procurement"}),
            ("portal_cppp", "Central Public Procurement Portal (CPPP)", {"jurisdiction": "National India", "type": "Tenders"})
        ]
        for port_id, name, props in portals:
            self.add_node(port_id, "Portal", name, props)

        # 4. Links between departments and competitors
        self.add_relationship("rel1", "dept_sales", "portal_gem", "MONITORS")
        self.add_relationship("rel2", "dept_sales", "portal_cppp", "MONITORS")

    def add_node(self, node_id: str, node_type: str, name: str, properties: Dict[str, Any] = None):
        self.vertices[node_id] = {
            "id": node_id,
            "type": node_type,
            "name": name,
            "properties": properties or {}
        }
        logger.info(f"[GraphStore] Added Node: [{node_type}] {name}")

    def add_relationship(self, edge_id: str, source: str, target: str, label: str, properties: Dict[str, Any] = None):
        if source in self.vertices and target in self.vertices:
            self.edges.append({
                "id": edge_id,
                "source": source,
                "target": target,
                "label": label,
                "properties": properties or {}
            })
            logger.info(f"[GraphStore] Added Relationship: {source} --({label})--> {target}")
        else:
            logger.warning(f"[GraphStore] Failed to connect edges: {source} or {target} missing.")

    def query_graph_structure(self) -> Dict[str, Any]:
        """Returns the full nodes and links structured for D3.js or HTML Canvas visualizations"""
        nodes = []
        for v in self.vertices.values():
            nodes.append({
                "id": v["id"],
                "label": v["name"],
                "type": v["type"],
                "properties": v["properties"]
            })
        
        links = []
        for e in self.edges:
            links.append({
                "id": e["id"],
                "source": e["source"],
                "target": e["target"],
                "label": e["label"]
            })
            
        return {"nodes": nodes, "links": links}
