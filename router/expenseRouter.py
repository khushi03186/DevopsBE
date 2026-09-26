# expenseRouter.py
from fastapi import APIRouter, Response
from model import Expense
from controller.expenseController import add_expense, get_expenses_by_user, delete_expense, update_expense

expense_router = APIRouter(tags=["Expenses"])

@expense_router.post("/expenses")
async def create_expense(data: Expense, response: Response):
    return await add_expense(data, response)

@expense_router.get("/expenses/user/{userId}")
async def fetch_user_expenses(userId: str, response: Response):
    return await get_expenses_by_user(userId, response)

@expense_router.delete("/expenses/{eid}")
async def remove_expense(eid: str, response: Response):
    return await delete_expense(eid, response)

@expense_router.put("/expenses/{eid}")
async def edit_expense(eid: str, data: Expense, response: Response):
    return await update_expense(eid, data, response)