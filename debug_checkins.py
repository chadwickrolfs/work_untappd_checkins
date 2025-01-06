from pathlib import Path
import json


all_checkins = json.loads(Path("db/checkins.json").read_text())

checkin_0_0 = all_checkins[0]['response']['checkins']['items'][0]
print(f"checkins type: {type(all_checkins)}")
print(f"checkins len: {len(all_checkins)}")
print(f"checkins[0] type: {type(all_checkins[0])}")
print(f"checkins[0] keys: {all_checkins[0].keys()}")
print("\nall_checkins[0] values types: \n"
      f"{[type(v) for v in all_checkins[0].values()]}\n"
      )
print(f"all_checkins[0] beer: {checkin_0_0['beer']}")
print(f"all_checkins[0] beer name: {checkin_0_0['beer']['beer_name']}")
print(f"all_checkins[0] beer abv: {checkin_0_0['beer']['beer_abv']}")
print(f"all_checkins[0] checkin_id: {checkin_0_0['checkin_id']}")

bierlist = [
    (checkin["checkin_id"], checkin["created_at"])
    for checkin_list in all_checkins
    for checkin in checkin_list["response"]["checkins"]["items"]
]
print(f"eerst: {bierlist[0]}\nlaatst: {bierlist[-1]}")
