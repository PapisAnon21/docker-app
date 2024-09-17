from fastapi import FastAPI
from userRoutes import router 

app = FastAPI()
app.include_router(router, prefix="/user")


@app.get("/", tags=["Home"])
async def home():
    return {"message" : "You're in home place"}