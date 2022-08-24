import os
import subprocess


def main():
    DOCKERFILE_DIR = "/app/src/dockerfile-template"
    dockerfiles:list[str] = os.listdir(DOCKERFILE_DIR)

    for dockerfile in dockerfiles:
        imagename = dockerfile.replace(".Dockerfile","")

        subprocess.run(f"docker build -t pyhouse-{imagename} -f {DOCKERFILE_DIR}/{dockerfile} .", shell=True, check=True)
  

if __name__ == "__main__":
    main()