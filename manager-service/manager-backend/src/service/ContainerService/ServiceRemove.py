import docker #type:ignore
from docker import DockerClient

docker_client = DockerClient.from_env()

def remove_service(name_in:str)->bool:
    for service in docker_client.services.list():
        print(service.attrs)
        if name_in in service.attrs['Spec']['Name']:
            service.remove()
            return True

    return False
