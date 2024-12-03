from fastapi import APIRouter, Body

from userModels import UserModel
import userCRUD
router = APIRouter()


@router.get("/get_users", tags=["Obtenir les users"])
async def get_users():
<<<<<<< HEAD
    return "test without database"

@router.get("/get_user/prenom/{prenom}", tags=["Cherecher un user par son prenom"])
async def get_user(prenom):
    return "test without database"

@router.get("/get_user/id/{id}", tags=["Cherecher un user par son id"])
def get_user_id(id):
    return "test without database"
=======
    return userCRUD.get_users()

@router.get("/get_user/prenom/{prenom}", tags=["Cherecher un user par son prenom"])
async def get_user(prenom):
    return userCRUD.get_user_prenom(prenom)

@router.get("/get_user/id/{id}", tags=["Cherecher un user par son id"])
def get_user_id(id):
    return userCRUD.get_user_id(id)
>>>>>>> 22ce99b8fc8905e6660966527b0ba0a01324eaad

@router.post("/create_user", tags=["Creer un User"])
def add_user(user : UserModel = Body(...)):
    #user = jsonable_encoder(user)
    print(user)
<<<<<<< HEAD
    user_create = "test without database"
=======
    user_create = userCRUD.create_user(user)
>>>>>>> 22ce99b8fc8905e6660966527b0ba0a01324eaad
    if(user_create):
        return user_create
    return "User not created !!"


