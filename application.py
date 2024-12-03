from fastapi import FastAPI
from userRoutes import router 

app = FastAPI()
app.include_router(router, prefix="/user")


@app.get("/", tags=["Home"])
async def home():
    return {"message" : "Vous etes sur la page d'acceuil . Ajoutez à l'url /docs pour voir le swagger en place"}