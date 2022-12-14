from __future__ import annotations
import argon2
from fastapi import FastAPI, HTTPException, Response, Cookie, Request, Header
from fastapi.responses import RedirectResponse
import pymongo
from pymongo.errors import DuplicateKeyError
from config import BASE_PATH, LASTEST_PASSWORD_ALG
from pydantic import BaseModel
from mongo_service import MongoService
from datetime import datetime
from typing import Any
from argon2 import PasswordHasher
from hashlib import sha256
from passlib.hash import phpass  # type:ignore
import secrets
import uuid
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

password_hasher = PasswordHasher()
MongoService.init_db()
app = FastAPI(docs_url=None)


class UserInput(BaseModel):
    username: str
    email: str
    password: str


class User(UserInput):
    user_id:str
    user_type: str
    extended_permissions:list
    is_activated: bool
    register_data: float
    alg: str

    @staticmethod
    def from_user_input(user_input: UserInput) -> User:
        user = User(**user_input.dict(),
                    user_id=str(uuid.uuid4()),
                    user_type="NORMAL_USER",
                    extended_permissions=[],
                    is_activated=False,
                    register_data=datetime.now().timestamp(),
                    alg=LASTEST_PASSWORD_ALG)

        user.password = password_hasher.hash(user.password)
        return user

    def save_to_db(self) -> None:
        data: dict[str, Any] = self.dict()
        MongoService.get_user_collection_instance().insert_one(data)


@app.post("/internal/register")
def register(user_input: UserInput):
    try:
        User.from_user_input(user_input).save_to_db()
    except DuplicateKeyError:
        raise HTTPException(400, detail="duplicated username")
    return {"result": 1}


# TODO: activate account

class LoginInput(BaseModel):
    username: str
    password: str


@app.get(BASE_PATH+"/login")
def login(username: str, password: str, resp:Response)->dict:
    user: User
    q = MongoService.get_user_collection_instance().find_one(
        {'username': username})
    if q is None:
        raise HTTPException(400, detail="username and password are incorrect.")
    user = User(**q)
    
    try:
        password_hasher.verify(user.password, password)
    except (argon2.exceptions.InvalidHash,argon2.exceptions.VerifyMismatchError):
        raise HTTPException(400,detail="username and password are incorrect.")
    session_id = secrets.token_urlsafe(32)
    MongoService.get_user_session_instance().insert_one({
        "session_id":hash_function(session_id),
        "user_id":user.user_id,
        "created_time":datetime.utcnow()
    }) 
    resp.set_cookie("session_id",session_id)


    return {"result":1}




@app.put("/internal/reset-password")
def forget_mypassword_verify_token(username:str,new_password:str):
    
    
    q = MongoService.get_user_collection_instance().find_one_and_update(
        {"username": username},
        {"$set": {"password": password_hasher.hash(new_password),
        'alg':LASTEST_PASSWORD_ALG}}
    )
    if q is None:
        raise HTTPException(404, detail="user not found")
    return {"result":1}


def hash_function(data: str) -> str:
    return sha256(data.encode("utf-8")).hexdigest()


def hash_verify(hash1: str, hash2: str) -> bool:
    bools: list[bool] = []
    for h1, h2 in zip(hash1, hash2):
        bools.append(h1 == h2)
    return all(bools)



def update_session(session_id:str):
    q = MongoService.get_user_session_instance().find_one_and_update(
        {
            "session_id": hash_function(session_id)
        },
        {
            "$set":{"created_time":datetime.utcnow()}
        }
    
    )
    if q is None:
        raise HTTPException(404,"session not found")

@app.get('/internal/container/auth')
def container_auth( head:str=Header(default="",alias="X-Forwarded-Uri"), session_id:str = Cookie(default="")):
    username = head.split("/")[2]
    container_name:str = head.split("/")[3]
  
    user = MongoService.get_user_session_instance().find_one({"session_id":hash_function(session_id)})
    if user is None:
        raise HTTPException(404,"session not found")
    user_id:str = user['user_id']
    q = MongoService.get_user_collection_instance().find_one({"user_id":user_id})

    if q is None:
        raise HTTPException(404,"session not found")
    q_username = q['username']
    if q_username != username:
        raise HTTPException(404,"session not found")

    update_session(session_id)

    return {"user_id":q['user_id']}
    
@app.get('/internal/who_are_they')
def who_are_they(session_id:str):
    q_session = MongoService.get_user_session_instance().find_one({
        "session_id":hash_function(session_id)
    })
    if q_session is None:
        raise HTTPException(404,"session not found")
    update_session(session_id)
    user_id = q_session["user_id"]

    q_user = MongoService.get_user_collection_instance().find_one({
        "user_id":user_id
    })
    if q_user is None:
        raise HTTPException(404,"user not found")
    username = q_user["username"]
    return {
        "user_id":user_id,
        "username":username
    }

    