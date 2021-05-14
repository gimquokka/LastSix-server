from flask import Flask, request
import pymongo
from models.garbage import Garbage
from flask_cors import CORS
import os

application = Flask(__name__)
CORS(application, resources={r"/*": {"origins": "*"}})

application.config['JSON_AS_ASCII'] = False

client = pymongo.MongoClient(os.environ['MONGO_HOST'])

level_distance = {
    1: 20,
    2: 30,
    3: 50,
    4: 100,
    5: 250,
    6: 500,
    7: 1000,
    8: 2000,
    9: 4000,
    10: 8000,
    11: 16000,
    12: 32000,
    13: 64000,
    14: 128000
}


@application.route("/<string:hpid>", methods=["GET"])
def find_one(hpid):
    garbage_model = Garbage(client)
    garbage = garbage_model.find_one(
        hpid,
        {
            "name": 1,
            "addr": 1,
            "tel": 1,
            "start": 1,
            "close": 1,
            "_id": 0,
        },
    )

    return {
        "msg": "success",
        "result": garbage,
    }


@application.route("/", methods=["GET"])
def find_all_closest():
    # not (A and B) = not A or not B
    if "lat" not in request.args or "lng" not in request.args:
        return {
            "msg": "failed",
            "detail": "lat and lng must be included in the query",
        }, 400

    garbage_model = Garbage(client)

    lat = float(request.args.get("lat", 37.5666805))
    lng = float(request.args.get("lng", 126.9784147))
    limit = int(request.args.get('limit', 10))

    closest_garbages = garbage_model.find_all_closest(
        lat,
        lng,
        limit,
        {
            "_id": 0,
            "name": 1,
            "location.coordinates": 1,
            "hpid": 1,
            "is_official": 1,
        }
    )

    for closest_garbage in closest_garbages:
        closest_garbage['isOfficial'] = closest_garbage.pop('is_official')
        coordinates = closest_garbage.pop('location')['coordinates']
        closest_garbage['lng'] = coordinates[0]
        closest_garbage['lat'] = coordinates[1]

    return {
        "msg": "success",
        "result": closest_garbages,
    }


if __name__ == "__main__":
    application.run(host="0.0.0.0")
