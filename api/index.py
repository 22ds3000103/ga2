from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
from pathlib import Path

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["GET"],  # Allows only GET requests
    allow_headers=["*"],  # Allows all headers
)

# Load the JSON data
data_path = Path(__file__).parent.parent / "q-vercel-python.json"
with open(data_path, "r") as file:
    data = json.load(file)

@app.get("/api")
async def get_marks(name: list[str] = Query(None)):
    if not name:
        return {"marks": []}
    
    marks = []
    for student_name in name:
        mark = None
        for entry in data:
            if entry["name"] == student_name:
                mark = entry["marks"]
                break
        marks.append(mark if mark is not None else 0)
    
    return {"marks": marks}
