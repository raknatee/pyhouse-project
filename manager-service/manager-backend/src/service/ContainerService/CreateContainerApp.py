from enum import Enum
import subprocess
from fastapi import APIRouter, Request, HTTPException
import requests
from pydantic import BaseModel

from config import BASE_PATH
from service.ContainerService.ComposeMode import ComposeMode
from service.ContainerService.ServiceGenerator import create_service

app = APIRouter()




class ContainerInfo(BaseModel):
    docker_compose_mode:ComposeMode
    docker_image_name:str
    attach_gpu:bool

@app.post(BASE_PATH+"/create_container")
def create_new_container(container_info:ContainerInfo):
    # TODO: authc authz

    create_service(
        container_info.docker_compose_mode,
        container_info.docker_image_name,
        "a"
    )




    
    