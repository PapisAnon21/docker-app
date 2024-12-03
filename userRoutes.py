from fastapi import APIRouter, Body

from userModels import UserModel
#import userCRUD
router = APIRouter()


@router.get("/get_users", tags=["Obtenir les users"])
async def get_users():
    return "test without database"

@router.get("/get_user/prenom/{prenom}", tags=["Cherecher un user par son prenom"])
async def get_user(prenom):
    return "test without database"

@router.get("/get_user/id/{id}", tags=["Cherecher un user par son id"])
def get_user_id(id):
    return "test without database"

@router.post("/create_user", tags=["Creer un User"])
def add_user(user : UserModel = Body(...)):
    #user = jsonable_encoder(user)
    print(user)
    user_create = "test without database"
    if(user_create):
        return user_create
    return "User not created !"


