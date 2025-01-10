""" untappd """
from pathlib import Path
import json


from fastapi import FastAPI


app = FastAPI()


db_dir = "db"
db_path = Path(db_dir)
just_checkins_file = "just_checkins.json"
just_checkins_path = Path(just_checkins_file)
checkins = json.loads((db_path/just_checkins_path).read_text())


@app.get("/")
async def get0():
    return {
        k: v for k, v in checkins.items()
        if k in [k for k in checkins.keys()][0:5]
    }
    # return checkins[0:5]


@app.get("/next")
async def nexts(skip: int = 0, limit: int = 10):
    """ http "127.0.0.1:8000/next?skip=20&limit=5" """
    error = []
    checkins_last = len(checkins) - 1
    if skip < 0 or skip > checkins_last:
        error.append(f"skip too great or small: {skip}")
    if limit < 0:
        error.append(f"limit {limit}: less than 0")
    if skip + limit > checkins_last:
        limit = checkins_last

    if error:
        return {"error": " ".join(error)}

    return {
        k: v for k, v in checkins.items()
        if k in [k for k in checkins.keys()][skip: skip + limit]
    }
    # return checkins[skip: skip + limit]


@app.get("/all")
async def all():
    return checkins
