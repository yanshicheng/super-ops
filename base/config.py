import os
import configparser
from django.conf import settings
config = configparser.ConfigParser()
config.read(r'config/config.ini')


def get_config(section, key):
    return config.get(section, key)
