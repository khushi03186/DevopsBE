# db.py
from motor.motor_asyncio import AsyncIOMotorClient

mongoURL = "mongodb+srv://admin:admin@cluster0.gf81tdr.mongodb.net/?appName=Cluster0"

client = AsyncIOMotorClient(mongoURL, tls=True,)

database = client["ExpenseDB"]

user_collection = database["users"]
expense_collection = database["expense tracker"]
