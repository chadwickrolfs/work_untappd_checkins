from pathlib import Path
import json


db = Path("db/checkins.json")
with open(db, "r") as dbh:
    checkins = json.load(dbh)

print(f"checkins type: {type(checkins)}")
print(f"checkins len: {len(checkins)}")
print(f"checkins[0] type: {type(checkins[0])}")
print(f"checkins[0] keys: {checkins[0].keys()}")
print("\ncheckins[0] values types: \n"
      f"{[type(v) for v in checkins[0].values()]}\n"
      )
print(f"checkins[0] beer: {checkins[0]['beer']}")
print(f"checkins[0] beer name: {checkins[0]['beer']['beer_name']}")
print(f"checkins[0] beer abv: {checkins[0]['beer']['beer_abv']}")
print(f"checkins[0] checkin_id: {checkins[0]['checkin_id']}")

checks = {checkin["checkin_id"]: checkin["created_at"] for checkin in checkins}
bierlist = [
    (checkin["checkin_id"], checkin["created_at"])
    for checkin in checkins
]
print(f"eerst: {bierlist[0]}\nlaatst: {bierlist[-1]}")
