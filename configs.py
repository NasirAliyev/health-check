import os
from os.path import join, dirname
from dotenv import load_dotenv

path = join(dirname(__file__), '.env')
load_dotenv(path)

ALARM_URL = os.environ.get("ALARM_URL")
BASE_URL = os.environ.get("BASE_URL")
