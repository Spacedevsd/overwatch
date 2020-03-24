from pymongo import MongoClient


class DB:
    def __init__(self, host="localhost", port="27017"):
        self.host = host
        self.port = port
        self.session = None

    def __enter__(self):
        if self.session is not None:
            raise RuntimeError("Already connected")
        self.session = MongoClient(f"mongodb://{self.host}:{self.port}")
        return self.session.overwatch

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        self.session = None

    # def save(self, instance):
    #     if not isinstance(instance, dict):
    #         raise TypeError("The instance should be a dict type")
    #     self.session.overwatch["heroes"].insert(instance)
