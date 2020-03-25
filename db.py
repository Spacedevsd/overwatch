from pymongo import MongoClient
from configparser import ConfigParser
from config import load

configuration = load()


class DB:
    def __init__(self):
        self.session = None

    def __enter__(self):
        _host = configuration.get("database", "host")
        _port = configuration.get("database", "port")

        if self.session is not None:
            raise RuntimeError("Already connected")
        self.session = MongoClient(f"mongodb://{_host}:{_port}")
        return self.session.overwatch

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        self.session = None

    # def save(self, instance):
    #     if not isinstance(instance, dict):
    #         raise TypeError("The instance should be a dict type")
    #     self.session.overwatch["heroes"].insert(instance)
