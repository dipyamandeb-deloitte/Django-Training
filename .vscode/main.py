from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Union
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Session
from model.table import User, Metrics
from database import con
from model.index import Hashers, Description

app = FastAPI()



@app.get('/metrics/')
async def search(id):
    data = con.execute(Description.select().where(Description.c.id.like('%' + search + '%')).fetchall())
    return {
        "success": True,
        "data": data
    }


@app.get('/metrics/{title}')
async def search(title):
    data = con.execute(Description.select().where(Description.c.title.like('%' + search + '%')).fetchall())
    return {
        "success": True,
        "data": data
    }


@app.get('/metrics/{description}')
async def search(decription):
    data = con.execute(Description.select().where(Description.c.description.like('%' + search + '%')).fetchall())
    return {
        "success": True,
        "data": data
    }


@app.post("users/{metrics}")
async def store(table: User):
    data = con.execute(Hashers.insert().values(
        name=Hashers.name,
        email=Hashers.email
    ))
    if data.is_insert:
        return {
            "success": True,
            "msg:": "user created successfully"
        }
    else:
        return {
            "success": False,
            "msg": "user not created"
        }


@app.patch('/users/')
async def update(id: int, table: User):
    data = con.execute(Hashers.update().values(
        name=Hashers.name,
        email=Hashers.email
    ).where(Hashers.c.id == id))

    if data:
        return {
            "success": True,
            "msg:": "user updated successfully"
        }
    else:
        return {
            "success": False,
            "msg": "user not updated "
        }


@app.delete("users/")
async def delete(id: int):
    data = con.execute(Hashers.delete().where(Hashers.c.id == id))
    if data:
        return {
            "success": True,
            "msg:": "user deleted successfully"
        }
    else:
        return {
            "success": False,
            "msg": "user not deleted"
        }
