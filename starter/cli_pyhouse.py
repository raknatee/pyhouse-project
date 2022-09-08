from __future__ import annotations
import subprocess
from enum import Enum
import sys
import os
from build_base_image.main import main as build_base_image_main
import docker #type:ignore
from docker import DockerClient

PROJECT_NAME = 'pyhouse'
def main(mode:Mode)->None:
    directory:str = f"../compose-files/{mode.value}".lower()
    compose_files:list[str] = os.listdir(directory)
  
    compose_files = [ os.path.join(directory,f) for f in compose_files]

    match mode:
        case Mode.DEV | Mode.PROD_WITHOUT_TLS:
            for compose_file in compose_files:
                subprocess.run(f"docker compose -f {compose_file} build", shell=True, check=True)
                subprocess.run(f"docker stack deploy -c {compose_file} {PROJECT_NAME}", shell=True, check=True)

        case Mode.PROD:
            raise NotImplemented

class Mode(Enum):
    DEV:str = 'DEV'
    PROD_WITHOUT_TLS = "PROD_WITHOUT_TLS"
    PROD:str = 'PROD'

    # @staticmethod
    # def factory(data:str)->Mode:
    #     data = data.upper()
    #     if data == Mode.DEV.value:
    #         return Mode.DEV
    #     if data == Mode.PROD.value:
    #         return Mode.PROD
    #     raise RuntimeError()


def login_to_admin_shell():
    docker_client:DockerClient = docker.from_env()
    for container in docker_client.containers.list():
        if "pyhouse_admin-shell" in container.name:
            subprocess.run(f"docker exec -it {container.id} bash",shell=True)
if __name__ == "__main__":

        std_input:int = int(input("""
\033[34;47;5mPYHOUSE CLI\033[0m
- Init Pyhouse
1. Dev
2. Prod without TLS (For demo)
3. Prod
4. remove all pyhouse's service

- Image Management
5. build based Image

- Go to Admin Shell
6. login to Admin Shell

Enter mode (number): """))

        match std_input:
            case 1:
                main(Mode.DEV)
            case 2:
                main(Mode.PROD_WITHOUT_TLS)
            case 3:
                main(Mode.PROD)
            case 4:
                subprocess.run("docker stack rm pyhouse", shell=True, check=True)
            case 5:
                build_base_image_main()
            case 6:
                login_to_admin_shell()

        
