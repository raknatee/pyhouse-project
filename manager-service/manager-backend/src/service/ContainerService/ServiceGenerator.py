import subprocess
import random
import os
from service.ContainerService.CreateContainerApp import ComposeMode


def create_service(mode:ComposeMode,image_name:str,username:str):
    filename = random.randint(0,9999)
    container_name:str = f"{username}-{filename}"
    with open(f"/tmp/{filename}.yaml","w") as docker_compose_file:
        with open(f"./compose-template/docker-compose-{mode.value}.yaml","r") as template:
            compose_template = template.read()

            docker_compose_file.write(
                compose_template
                .replace("{container_name}",container_name)
                .replace("{image_name}",image_name)
                .replace("{username}",username)
                .replace("{ROOT_PROJECT}",os.environ["ROOT_PROJECT"])
            )

    subprocess.run(f"docker stack deploy pyhouse -c /tmp/{filename}.yaml", shell=True, check=True)