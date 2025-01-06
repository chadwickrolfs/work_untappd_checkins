from pathlib import Path
import json


all_checkins = json.loads(Path("db/checkins.json").read_text())

checks = {
    checkin["checkin_id"]: checkin["created_at"]
    for checkin_list in all_checkins
    for checkin in checkin_list["response"]["checkins"]["items"]
}
bierlist = [
    (checkin["checkin_id"], checkin["created_at"])
    for checkin_list in all_checkins
    for checkin in checkin_list["response"]["checkins"]["items"]
]
