from pymongo import MongoClient
from configparser import ConfigParser


class DB:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read("database.ini")
        self.session = None

    def __enter__(self):
        _host = self.config.get("development", "host")
        _port = self.config.get("development", "port")

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
