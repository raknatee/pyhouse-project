from fastapi import APIRouter, Request, HTTPException
import requests
from pydantic import BaseModel

from config import BASE_PATH
from service.UserServices.UserAuthc import check_and_get_client_info

app = APIRouter()


@app.get(BASE_PATH+"/who_am_i")
def who_am_i(req:Request):
    return check_and_get_client_info(req)

    
    