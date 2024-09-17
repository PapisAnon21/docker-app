from pydantic import BaseModel

class UserModel(BaseModel):
    prenom : str
    nom : str
    age : int
    fonction : str