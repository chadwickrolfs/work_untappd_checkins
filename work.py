from pathlib import Path
import json


db_dir = "db"
db_path = Path(db_dir)
checkins_file = "checkins.json"
checkins_path = Path(checkins_file)
just_checkins_file = "just_checkins.json"
just_checkins_path = Path(just_checkins_file)

all_checkins = json.loads((db_path/checkins_path).read_text())

just_checkins = [
    checkin
    for checkin_list in all_checkins
    for checkin in checkin_list["response"]["checkins"]["items"]
]
bierlijst = []
for checkin in just_checkins:
    venue = checkin.get("venue")
    venue_id = 0 if venue == [] else venue.get("venue_id")
    venue_name = "" if venue == [] else venue.get("venue_name")
    venue_address = "" if venue == [] else venue.get(
        "location").get("venue_address")
    venue_city = "" if venue == [] else venue.get(
        "location").get("venue_city")
    venue_country = "" if venue == [] else venue.get(
        "location").get("venue_country")
    venue_lat = 0.0 if venue == [] else venue.get(
        "location").get("lat")
    venue_lon = 0.0 if venue == [] else venue.get(
        "location").get("lng")

    bierlijst.append({
        "checkin_id": checkin["checkin_id"],
        "checkin_datetime": checkin["created_at"],
        "checkin_comment": checkin["checkin_comment"],
        "beer_bid": checkin["beer"]["bid"],
        "beer_name": checkin["beer"]["beer_name"],
        "beer_abv": checkin["beer"]["beer_abv"],
        "beer_style": checkin["beer"]["beer_style"],
        "brewery_id": checkin["brewery"]["brewery_id"],
        "brewery_name": checkin["brewery"]["brewery_name"],
        "brewery_country": checkin["brewery"]["country_name"],
        "brewery_city": checkin["brewery"]["location"]["brewery_city"],
        "brewery_latitude": checkin["brewery"]["location"]["lat"],
        "brewery_longitude": checkin["brewery"]["location"]["lng"],
        "venue_id": venue_id,
        "venue_name": venue_name,
        "venue_address": venue_address,
        "venue_city": venue_city,
        "venue_country": venue_country,
        "venue_latitude": venue_lat,
        "venue_longitude": venue_lon,
    })

(db_path/just_checkins_path).write_text(json.dumps(bierlijst))
