from __future__ import annotations
import subprocess
from enum import Enum
import sys
import os
from build_base_image.main import main as build_base_image_main

PROJECT_NAME = 'pyhouse'
def main(mode:Mode)->None:
    directory:str = f"../compose-files/{mode.value}".lower()
    compose_files:list[str] = os.listdir(directory)
  
    compose_files = [ os.path.join(directory,f) for f in compose_files]

    if mode == Mode.DEV:
        for compose_file in compose_files:
            subprocess.run(f"docker compose -f {compose_file} build", shell=True, check=True)
            subprocess.run(f"docker stack deploy -c {compose_file} {PROJECT_NAME}", shell=True, check=True)


    if mode == Mode.PROD:
        raise NotImplemented
        for compose_file in compose_files:
            subprocess.run(f"docker compose -f {compose_file} build", shell=True, check=True)
            subprocess.run(f"docker stack deploy -c {compose_file} {PROJECT_NAME}", shell=True, check=True)
    
class Mode(Enum):
    DEV:str = 'DEV'
    PROD:str = 'PROD'

    @staticmethod
    def factory(data:str)->Mode:
        data = data.upper()
        if data == Mode.DEV.value:
            return Mode.DEV
        if data == Mode.PROD.value:
            return Mode.PROD
        raise RuntimeError()
if __name__ == "__main__":
    
    std_input:int = int(input("""- Init Pyhouse
1. Dev
2. Prod
3. remove all pyhouse's service

- Image Management
4. build based Image
Enter mode (number): """))

    match std_input:
        case 1:
            main(Mode.DEV)
        case 2:
            main(Mode.PROD)
        case 3:
            subprocess.run("docker stack rm pyhouse", shell=True, check=True)
        case 4:
            build_base_image_main()
