# api/index.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
from pathlib import Path

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load the JSON data
data_path = Path(__file__).parent.parent / "q-vercel-python.json"
with open(data_path, "r") as file:
    data = json.load(file)

# Create a dictionary for O(1) lookup
marks_dict = {entry["name"]: entry["marks"] for entry in data}

@app.get("/api")
async def get_marks(name: list[str] = Query(None)):
    if not name:
        return {"marks": []}
    
    # Get marks in the exact order of requested names
    marks = [marks_dict.get(student_name, 0) for student_name in name]
    return {"marks": marks}
