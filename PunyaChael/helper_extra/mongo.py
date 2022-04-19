
import asyncio
import sys
import os 

from motor import motor_asyncio
from odmantic import AIOEngine
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


MONGO_URI = os.environ.get("MONGO_URI")
MONGO_PORT = os.environ.get("MONGO_PORT")
MONGO_DB = os.environ.get("MONGO_DB")

# Init MongoDB
mongodb = MongoClient(MONGO_URI, MONGO_PORT)[MONGO_DB]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_URI, MONGO_PORT)
db = motor[MONGO_DB]



