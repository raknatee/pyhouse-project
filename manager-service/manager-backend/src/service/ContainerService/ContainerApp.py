from enum import Enum
import subprocess
from fastapi import APIRouter, Request, HTTPException
import requests
from pydantic import BaseModel

from config import APPLICATION_MODE, BASE_PATH

from service.ContainerService.ServiceGenerator import create_service
from service.ContainerService.ServiceRemove import remove_service
from service.UserServices.UserAuthc import check_and_get_client_info

app = APIRouter()

import docker #type:ignore
from docker import DockerClient 
docker_client = DockerClient.from_env()


class ContainerInfo(BaseModel):
    docker_image_name:str
    attach_gpu:bool

@app.post(BASE_PATH+"/create_container")
def create_new_container(req:Request,container_info:ContainerInfo):
    # TODO:  authz
    username = check_and_get_client_info(req).username
    create_service(
        APPLICATION_MODE,
        container_info.docker_image_name,
        username
    )
    return {"result":1}

@app.get(BASE_PATH+"/containers")
def search_containers_endpoit(req:Request):
    # TODO:  authz
    username = check_and_get_client_info(req).username


    return {"services":search_containers(username)}

@app.get(BASE_PATH+"/container")
def get_container_status_endpoit(req:Request,filter_name:str):
    # TODO:  authz
    username = check_and_get_client_info(req).username
    for container in docker_client.containers.list():
        if filter_name in container.attrs['Name']:
            return {"ok":True}
        

    raise HTTPException(404)

@app.delete(BASE_PATH+"/container")
def remove_service_endpoint(req:Request,filter_name:str):
    # TODO: authz
    username = check_and_get_client_info(req)
    ok:bool = remove_service(filter_name)
    if not ok:
        raise HTTPException(400)
    return {"result":1}


def search_containers(username:str)->list[tuple[str,str]]:

    containers = docker_client.services.list()
    returned:list[tuple[str,str]] = []
    for container in containers:
        service_name:str = container.attrs["Spec"]["Name"]
        container_name:str = service_name.replace("pyhouse_user-container-","")
        username_container:str = container_name.split("-")[0]
        based_image:str = container.attrs["Spec"]["Labels"]["com.docker.stack.image"]
        if(username == username_container):
            returned.append((container_name,based_image))

    return returned 


    