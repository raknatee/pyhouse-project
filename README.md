# PYHOUSE

## Concept
- Docker in Docker on Docker Swarm with Docker Host and also supports Docker Context which all of them are controlled by Python ???
 
## Installation
1. Docker


## Setup
```sh
docker swarm init --advertise-addr='xxx.xxx.xxx.xxx'
```

## Installation
```sh
docker compose up --build -d
docker compose exec starter bash
```
- Then, follows the CLI instruction
  - You need to build the Base Image first
    - If you wanted to modify Dockerfile, please did it before building the Image.
        ```sh
        cd ./starter/build_base_image/dockerfile-template
        vim {new dockerfile or template}.Dockerfile
        ```
  - Deploy


