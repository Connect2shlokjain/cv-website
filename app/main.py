from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
import json
import pathlib

BASE = pathlib.Path(__file__).resolve().parent
DATA_DIR = BASE / "data"

app = FastAPI()
app.mount("/static", StaticFiles(directory=str(BASE / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE / "templates"))

def load_json(name: str):
    p = DATA_DIR / name
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {}

@app.get("/")
async def home(request: Request):
    resume = load_json("resume.json")
    experience = load_json("experience.json")
    projects = load_json("projects.json")
    education = load_json("education.json")
    skills = load_json("skills.json")
    certificates = load_json("certificates.json")
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "resume": resume,
        "experience": experience,
        "projects": projects,
        "education": education,
        "skills": skills,
        "certificates": certificates
    })

@app.get("/api/resume")
async def api_resume():
    return JSONResponse({
        "resume": load_json("resume.json"),
        "experience": load_json("experience.json"),
        "projects": load_json("projects.json"),
        "education": load_json("education.json"),
        "skills": load_json("skills.json"),
        "certificates": load_json("certificates.json")
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
