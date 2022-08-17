FROM python:3.10.5-buster
WORKDIR /home/src
EXPOSE 8000

# install docker ce cli
ENV DEBIAN_FRONTEND="noninteractive"
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

# python deps

RUN pip install "uvicorn[standard]"
RUN pip install fastapi==0.79.0
RUN pip install argon2-cffi==21.3.0
RUN pip install pymongo==4.2.0
RUN pip install mypy
RUN pip install pytest
RUN pip install requests
RUN pip install passlib==1.7.4


COPY ./src .



CMD tail -f /dev/null

# CMD uvicorn main:app --host 0.0.0.0 --reload