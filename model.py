# model.py
from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    username: str
    email: str
    address: str
    gender: str
    password: str


class Login(BaseModel):
    username: str
    password: str


class Expense(BaseModel):
    userId: str 
    name: str
    cost: str
    payment: str
    description: str  