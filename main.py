# main.py
from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import Gender, Role, User
app = FastAPI()
db: List[User] = [
 User(
 id=uuid4(),
 first_name="Esteban",
 last_name="Diaczun",
 gender=Gender.male,
 roles=[Role.user],
 ),
 User(
 id=uuid4(),
 first_name="Flor",
 last_name="Tala",
 gender=Gender.female,
 roles=[Role.user],
 ),
 User(
 id=uuid4(),
 first_name="Lucas",
 last_name="Faso",
 gender=Gender.male,
 roles=[Role.user],
 ),
 User(
 id=uuid4(),
 first_name="Sofia",
 last_name="papi",
 gender=Gender.male,
 roles=[Role.admin, Role.user],
 ),
]

@app.post("/usuarios")
async def create_user(user: User):
    return {"id": user.id}

@app.get("/usuarios")
async def get_users():
 return db

@app.get("/")
async def root():
 return {"greeting":"Hello world"}






'''
POST: para crear datos.
GET: para leer datos.
PUT: para actualizar datos.
DELETE: para borrar datos.
'''