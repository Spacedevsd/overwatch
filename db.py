from pymongo import MongoClient


class Db:
    def __init__(self, host="localhost", port="27017"):
        self._client = MongoClient(f"mongodb://{host}:{port}")
        self._db = self._client.overwatch

    def insert(self, instance):
        if not isinstance(instance, dict):
            raise TypeError("The instance should be a dict type")
        self._db["heroes"].insert(instance)

    def close(self):
        self._client.close()
