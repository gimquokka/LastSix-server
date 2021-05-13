from flask import Flask, request
import pymongo
from models.garbege import Garbege

application = Flask(__name__)
client = pymongo.MongoClient("mongodb://localhost:27017/")


@application.route("/<string:hpid>", methods=["GET"])
def find_one(hpid):
    garbege_model = Garbege(client)
    garbege = garbege_model.find_one(
        hpid,
        {
            "name": 1,
            "addr": 1,
            "tel": 1,
            "start": 1,
            "end": 1,
            "_id": 0,
        },
    )
    return {
        "msg": "success",
        "result": garbege,
    }


@application.route("/", methods=["GET"])
def find_all_closest():
    # not (A and B) = not A or not B
    if "lat" not in request.args or "lng" not in request.args:
        return {
            "msg": "failed",
            "detail": "lat and lng must be included in the query",
        }, 400
    garbege_model = Garbege(client)
    lat = float(request.args.get("lat", 37.5666805))
    lng = float(request.args.get("lng", 126.9784147))
    closest_garbeges = garbege_model.find_all_closest(
        lat,
        lng,
        {
            "_id": 0,
            "name": 1,
            "lat": 1,
            "lng": 1,
            "hpid": 1,
            "is_official": 1,
        },
    )
    
    for closest_garbege in closest_garbeges:
        closest_garbege['isOfficial'] = closest_garbege.pop('is_official')
        
    return {
        "msg": "success",
        "result": closest_garbeges,
    }


if __name__ == "__main__":
    application.run(host="0.0.0.0")
