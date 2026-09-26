# expenseController.py
from fastapi import Response
from db import expense_collection
from model import Expense
from bson import ObjectId

async def add_expense(data: Expense, response: Response):
    try:
        res = await expense_collection.insert_one(data.dict())
        response.status_code = 201
        return {"success": True, "id": str(res.inserted_id)}
    except Exception as e:
        response.status_code = 500
        return {"success": False, "error": str(e)}

async def get_expenses_by_user(userId: str, response: Response):
    expenses = []
    try:
        cursor = expense_collection.find({"userId": userId})
        async for item in cursor:
            item["_id"] = str(item["_id"])
            expenses.append(item)
        return expenses
    except Exception as e:
        response.status_code = 500
        return {"success": False, "error": str(e)}

async def delete_expense(eid: str, response: Response):
    try:
        await expense_collection.delete_one({"_id": ObjectId(eid)})
        return {"success": True, "message": "Expense deleted"}
    except Exception as e:
        response.status_code = 500
        return {"success": False, "error": str(e)}


async def update_expense(eid: str, data: Expense, response: Response):
    try:
        update_result = await expense_collection.update_one(
            {"_id": ObjectId(eid)},
            {
                "$set": {
                    "name": data.name,
                    "cost": data.cost,
                    "payment": data.payment,
                    "description": data.description,
                    "userId": data.userId
                }
            }
        )

        if update_result.matched_count == 0:
            response.status_code = 404
            return {"success": False, "message": "Expense not found"}

        return {"success": True, "message": "Expense updated successfully"}

    except Exception as e:
        response.status_code = 500
        return {"success": False, "error": str(e)}

    
