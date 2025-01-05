from pathlib import Path
import json


checkins = json.loads(Path("db/checkins.json").read_text())

checkin_0_0 = checkins[0]['response']['checkins']['items'][0]
print(f"checkins type: {type(checkins)}")
print(f"checkins len: {len(checkins)}")
print(f"checkins[0] type: {type(checkins[0])}")
print(f"checkins[0] keys: {checkins[0].keys()}")
print("\ncheckins[0] values types: \n"
      f"{[type(v) for v in checkins[0].values()]}\n"
      )
print(f"checkins[0] beer: {checkin_0_0['beer']}")
print(f"checkins[0] beer name: {checkin_0_0['beer']['beer_name']}")
print(f"checkins[0] beer abv: {checkin_0_0['beer']['beer_abv']}")
print(f"checkins[0] checkin_id: {checkin_0_0['checkin_id']}")

checks = {
    checkin["checkin_id"]: checkin["created_at"]
    for checkin_list in checkins
    for checkin in checkin_list["response"]["checkins"]["items"]
}
bierlist = [
    (checkin["checkin_id"], checkin["created_at"])
    for checkin_list in checkins
    for checkin in checkin_list["response"]["checkins"]["items"]
]
print(f"eerst: {bierlist[0]}\nlaatst: {bierlist[-1]}")
