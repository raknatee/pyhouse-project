# docker-jupyterhub
 
## Installation
1. Docker
2. pipenv and Python3.10

## Setup
```sh
docker swarm init --advertise-addr='xxx.xxx.xxx.xxx'
docker exec -it {manager_container_id} pipenv run python src/build_base_image.py
```


