# userRouter.py
from fastapi import APIRouter, Response
from model import User, Login
from controller.userController import register_user, login_user

user_router = APIRouter(tags=["Users"])

@user_router.post("/register")
async def register(data: User, response: Response):
    return await register_user(data, response)

@user_router.post("/login")
async def login(data: Login, response: Response):
    return await login_user(data, response)
