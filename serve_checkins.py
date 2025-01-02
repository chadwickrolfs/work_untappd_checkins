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
    return checkins[skip: skip + limit]
