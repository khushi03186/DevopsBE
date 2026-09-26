# main.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from router.userRouter import user_router
from router.expenseRouter import expense_router
from utils import decode_access_token

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    if request.method == "OPTIONS":
        return await call_next(request)

    if request.url.path in ["/", "/login", "/register", "/docs"]:
        return await call_next(request)

    token = request.headers.get("Authorization")

    if not token:
        return JSONResponse(content={"message": "Token missing"}, status_code=401)

    token = token.replace("Bearer ", "")
    payload = decode_access_token(token, "your_secret_key")

    if not payload:
        return JSONResponse(content={"message": "Invalid token"}, status_code=403)

    request.state.user = payload
    return await call_next(request)


app.include_router(user_router)
app.include_router(expense_router)


@app.get("/")
def test():
    return {"message": "Expense Backend Running"}