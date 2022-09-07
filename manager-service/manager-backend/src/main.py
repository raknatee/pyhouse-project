from fastapi import FastAPI

from config import BASE_PATH

import docker # type:ignore
from docker import DockerClient

docker_client = DockerClient.from_env()
app = FastAPI()


@app.get(BASE_PATH)
def read_root():
    return {"Hello": "World"}

@app.get(BASE_PATH+"/images")
def get_pyhose_image()->dict[str,list[str]]:
    # TODO authc
    image_names:list[str] = []
    for image in docker_client.images.list():
        _image_name:list[str] = image.attrs["RepoTags"]
        if len(_image_name) == 0:
            continue
        image_name:str = ",".join(_image_name)
        if "pyhouse-image-global" in image_name:
            print(image_name)
            image_names.append(image_name)
    return {"images":image_names}





from service.UserServices.UserServiceApp import app as user_service_app
app.include_router(user_service_app)

from service.ContainerService.ContainerApp import app as docker_service_app
app.include_router(docker_service_app)