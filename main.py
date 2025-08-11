from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import yaml
import os
from typing import Dict, Any, List
from pydantic import BaseModel

app = FastAPI(title="Portfolio API", description="API for dynamic portfolio website")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="."), name="static")

class Project(BaseModel):
    id: str
    title: str
    tagline: str
    categories: List[str]
    tags: List[str]
    description: Dict[str, str]
    kpis: List[str]
    role: str
    links: Dict[str, str]

class Profile(BaseModel):
    name: str
    subtitle: str
    logo: str
    title: str
    description: str
    skills: List[str]

class Navigation(BaseModel):
    contact_email: str
    external_links: Dict[str, str]

class Filter(BaseModel):
    key: str
    label: str

class PortfolioData(BaseModel):
    profile: Profile
    navigation: Navigation
    projects: List[Project]
    filters: List[Filter]
    footer: Dict[str, str]

def load_config() -> Dict[str, Any]:
    """Load configuration from YAML file"""
    config_path = "portfolio_config.yaml"
    if not os.path.exists(config_path):
        raise HTTPException(status_code=500, detail="Configuration file not found")
    
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading configuration: {str(e)}")

@app.get("/")
async def serve_portfolio():
    """Serve the main portfolio HTML page"""
    return FileResponse("index.html")

@app.get("/api/portfolio", response_model=PortfolioData)
async def get_portfolio_data():
    """Get all portfolio data"""
    config = load_config()
    return PortfolioData(**config)

@app.get("/api/profile", response_model=Profile)
async def get_profile():
    """Get profile information"""
    config = load_config()
    return Profile(**config["profile"])

@app.get("/api/projects", response_model=List[Project])
async def get_projects():
    """Get all projects"""
    config = load_config()
    return [Project(**project) for project in config["projects"]]

@app.get("/api/projects/{project_id}", response_model=Project)
async def get_project(project_id: str):
    """Get a specific project by ID"""
    config = load_config()
    for project in config["projects"]:
        if project["id"] == project_id:
            return Project(**project)
    raise HTTPException(status_code=404, detail="Project not found")

@app.get("/api/navigation", response_model=Navigation)
async def get_navigation():
    """Get navigation data"""
    config = load_config()
    return Navigation(**config["navigation"])

@app.get("/api/filters", response_model=List[Filter])
async def get_filters():
    """Get filter options"""
    config = load_config()
    return [Filter(**filter_item) for filter_item in config["filters"]]

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "Portfolio API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)