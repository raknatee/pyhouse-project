FROM ubuntu:20.04

ENV DEBIAN_FRONTEND="noninteractive"

# install Python
RUN apt update -y && apt upgrade -y

RUN apt install -yfm --no-install-recommends libgl1-mesa-glx libgtk2.0-dev

RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa


RUN apt install python3.10 -y
RUN apt install python3-pip -y
RUN apt install python3.10-distutils -y
RUN pip3 install pipenv



WORKDIR /admin-shell
RUN mkdir .venv
RUN pipenv --python 3.10


RUN pipenv install mypy
RUN pipenv install requests
RUN pipenv install docker
RUN pipenv install types-requests

WORKDIR /admin-shell/src
COPY ./src .

RUN cat ./linux/extended_bashrc.sh >> ~/.bashrc

CMD tail -f /dev/null


