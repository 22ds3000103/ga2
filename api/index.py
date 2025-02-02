from fastapi import FastAPI, Query
import json
from pathlib import Path

app = FastAPI()

# Load the JSON data
data_path = Path(__file__).parent.parent / "q-vercel-python.json"
with open(data_path, "r") as file:
    data = json.load(file)

@app.get("/api")
async def get_marks(names: list[str] = Query(...)):
    results = []
    for name in names:
        for entry in data:
            if entry["name"] == name:
                results.append({"name": name, "marks": entry["marks"]})
                break
        else:
            results.append({"name": name, "marks": None})
    return results
