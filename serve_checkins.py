""" untappd """
from pathlib import Path
import json


from fastapi import FastAPI


app = FastAPI()


db = Path("db/checkins.json")
with open(db, "r") as dbh:
    checkins = json.load(dbh)


@app.get("/")
async def get0():
    return checkins[0-5]


@app.get("/next")
async def fakedb(skip: int = 0, limit: int = 10):
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

    return checkins[skip: skip + limit]
