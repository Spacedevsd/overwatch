from configparser import ConfigParser
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def load():
    config = ConfigParser()
    config.read("config.ini")
    return config
