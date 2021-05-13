"""
MongoDB garbage Collection Model
"""


class Garbage:
    def __init__(self, client):
        self.col = client["medicine"]["garbage"]

    def find_one(
        self,
        hpid,
        projection=None,
    ):
        return self.col.find_one(
            {"hpid": hpid},
            projection,
        )

    def find_all_closest(
        self,
        lat,
        lng,
        distance,
        limit,
        projection=None,
    ):
        return list(
            self.col.find(
                {
                    # location will replace into collection name
                    "location": {
                        "$near": {
                            "$geometry": {
                                "type": "Point",
                                "coordinates": [
                                    lng,
                                    lat,
                                ],
                            },
                            "$maxDistance": distance,
                        },
                    }
                },
                projection,
            ).limit(limit)
        )
