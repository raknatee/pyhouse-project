FROM ubuntu:20.04

ENV DEBIAN_FRONTEND="noninteractive"

# install docker ce cli

RUN apt-get update
RUN apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release -y
RUN mkdir -p /etc/apt/keyrings
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg |  gpg --dearmor -o /etc/apt/keyrings/docker.gpg
RUN echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" |  tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN  apt-get update
RUN  apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin -y


# install Python
RUN apt update -y && apt upgrade -y

RUN apt install -yfm --no-install-recommends libgl1-mesa-glx libgtk2.0-dev

RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa


RUN apt install python3.10 -y
RUN apt install python3-pip -y
RUN apt install python3.10-distutils -y
RUN pip3 install pipenv


RUN echo "alias pyv='pipenv run python'" >> ~/.bashrc


WORKDIR /app
RUN mkdir .venv
RUN pipenv --python 3.10


RUN pipenv install mypy
RUN pipenv install requests
RUN pipenv install docker
RUN pipenv install types-requests

WORKDIR /app/src
COPY . .

WORKDIR /app/src/starter


CMD tail -f /dev/null


