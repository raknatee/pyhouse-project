from __future__ import annotations
import subprocess
from enum import Enum
import sys
import os

PROJECT_NAME = 'pyhouse'
def main(mode:Mode, cmd:str)->None:
    directory:str = f"./compose-files/{mode.value}".lower()
    compose_files:list[str] = os.listdir(directory)
  
    compose_files = [ os.path.join(directory,f) for f in compose_files]

    if mode == Mode.DEV:
        compose_file:str = " ".join([f"-f {c}" for c in compose_files])
        subprocess.run(f"docker compose {compose_file} {cmd}", shell=True, check=True)
        

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

    mode:Mode
    cmd:str
    
    if len(sys.argv)>1 and ("--dev" in sys.argv[1] or "--prod" in sys.argv[1]):
        mode = Mode.factory(sys.argv[1].replace("--",""))
        if mode == Mode.DEV:
            cmd = " ".join(sys.argv[2:len(sys.argv)])
        if mode == Mode.PROD:
            cmd = ""
    else:
        mode = Mode.DEV
        cmd = " ".join(sys.argv[1:len(sys.argv)])

    main(mode,cmd)