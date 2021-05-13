"""
MongoDB garbege Collection Model
"""


class Garbege:
    def __init__(self, client):
        self.col = client["medicine"]["garbege"]

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
        projection=None,
    ):
        """
        진영님께서 여기에 query만들어 주시면 됩니다.
        """
        return list(
            self.col.find(
                {},
                projection,
            )
        )
