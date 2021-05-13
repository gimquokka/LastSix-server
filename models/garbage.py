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
        projection=None,
        limit=10,
    ):
        """
        진영님께서 여기에 query만들어 주시면 됩니다.
        """
        # return list(
        #     self.col.find({
        #         # locationt will replace into collection name
        #         "location": {
        #             "$geoWithin": {
        #                 # 1km 근방으로 조회 (map zoom in/out에 따라 수정 필요)
        #                 "$centerSphere": [[lng, lat], 500 / 6378.1]
        #             }
        #         }
        #     },
        #         projection,
        #     ).limit(limit)
        # )
        return list(
            self.col.find(
                {
                    # locationt will replace into collection name
                    "location": {
                        "$near": {
                            "$geometry": {"type": "Point", "coordinates": [lng, lat]},
                            "$maxDistance": distance,
                        },
                    }
                },
                projection,
            ).limit(limit)
        )
