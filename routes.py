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
    if "lat" not in request.args and "lng" not in request.args:
        return {
            "msg": "failed",
            "detail": "lat and lng must be included in the query",
        }, 400
    garbege_model = Garbege(client)
    lat, lng = float(request.args["lat"]), float(request.args["lng"])
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
    return {
        "msg": "success",
        "result": closest_garbeges,
    }


if __name__ == "__main__":
    application.run(host="0.0.0.0")
