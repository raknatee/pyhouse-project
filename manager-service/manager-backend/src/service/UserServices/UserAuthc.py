from fastapi import Request, HTTPException
import requests
from pydantic import BaseModel

class ClientInfo(BaseModel):
    user_id:str
    username:str

def check_and_get_client_info(req:Request)->ClientInfo:
    client_session_id:str 
    try:
        client_session_id = req.cookies['session_id']
    except KeyError:
        raise HTTPException(400)

    q = requests.get(f"http://auth-backend:8000/internal/who_are_they?session_id={client_session_id}")
    if q.status_code != 200:
        raise HTTPException(400)
    returned = ClientInfo(**q.json())
    return returned