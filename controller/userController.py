# userController.py
from fastapi import Response
from model import User, Login
from db import user_collection
from utils import hash_password, verify_password, create_access_token

SECRET_KEY = "your_secret_key"

async def register_user(data: User, response: Response):
    try:
        existing = await user_collection.find_one({"username": data.username})
        if existing:
            response.status_code = 400
            return {"success": False, "message": "User already exists"}

        user_dict = data.dict()
        user_dict["password"] = hash_password(data.password)

        res = await user_collection.insert_one(user_dict)
        response.status_code = 201
        return {
            "success": True,
            "userId": str(res.inserted_id),
            "message": "User registered successfully"
        }
    except Exception as e:
        response.status_code = 500
        return {"success": False, "error": str(e)}


async def login_user(data: Login, response: Response):
    try:
        user = await user_collection.find_one({"username": data.username})

        if not user:
            response.status_code = 401
            return {"success": False, "message": "Invalid username or password"}

        if not verify_password(data.password, user["password"]):
            response.status_code = 401
            return {"success": False, "message": "Invalid username or password"}

        token_data = {"userId": str(user["_id"]), "username": user["username"]}
        token = create_access_token(token_data, SECRET_KEY)

        return {
            "success": True,
            "message": "Login successful",
            "userId": str(user["_id"]),
            "token": token
        }

    except Exception as e:
        response.status_code = 500
        return {"success": False, "error": str(e)}



# async def login_user(data: Login, response: Response):
#     try:
#         user = await user_collection.find_one({"username": data.username})

#         if not user:
#             response.status_code = 401
#             return {"success": False, "message": "Invalid username or password"}

#         if not verify_password(data.password, user["password"]):
#             response.status_code = 401
#             return {"success": False, "message": "Invalid username or password"}

#         return {
#             "success": True,
#             "message": "Login successful",
#             "userId": str(user["_id"])
#         }

#     except Exception as e:
#         response.status_code = 500
#         return {"success": False, "error": str(e)}



