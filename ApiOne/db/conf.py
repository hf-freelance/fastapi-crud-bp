import motor.motor_asyncio
from bson import ObjectId


client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://127.0.0.1:27017/")
db_conf = client.fastdb


