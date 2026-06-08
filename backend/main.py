import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import router

app = FastAPI(
    title="TenderPilot AI: Autonomous Bid & Procurement Workforce",
    description="Multi-agent business development employee built for the Microsoft Build Hackathon 2026",
    version="1.0.0"
)

# Enable CORS for frontend dashboard connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount API routes
app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "TenderPilot AI Core",
        "hackathon": "Microsoft Build 2026",
        "agentic_web_theme": True,
        "tagline": "An AI Business Development Employee that finds, evaluates, and prepares government tender opportunities autonomously."
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
