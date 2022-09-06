FROM nvidia/cuda:11.6.0-devel-ubuntu20.04
WORKDIR /home/container
ENV TZ="Asia/Bangkok"

RUN apt update -y && apt upgrade -y
ENV DEBIAN_FRONTEND="noninteractive"

RUN apt install -yfm --no-install-recommends libgl1-mesa-glx libgtk2.0-dev

RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt install python3.10 -y
RUN apt install python3-pip -y
RUN apt install python3.10-distutils -y
RUN pip3 install pipenv

RUN mkdir /home/container/.venv
RUN pipenv --python 3.10

RUN pipenv install ipython==6.5.0
RUN pipenv install jupyterlab==3.4.4
RUN pipenv install torch==1.12.1
RUN pipenv install torchvision==0.13.1 
RUN pipenv install torchaudio==0.12.1
RUN pipenv install pillow==9.2.0 
RUN pipenv install opencv-python==4.6.0.66 
RUN pipenv install scikit-learn==1.1.2
RUN pipenv install pandas==1.4.3
RUN pipenv install seaborn==0.11.2
RUN pipenv install matplotlib==3.5.3
RUN pipenv install mypy==0.910 
RUN pipenv install pytest==6.2.5 
RUN pipenv install mne==1.1.1
RUN pipenv install scipy==1.9.0 

WORKDIR /home/container/src

# COPY ./jupyter_config /root/.jupyter
CMD tail -f /dev/null
# CMD pipenv run jupyter lab --ip='*' --port=8888 --no-browser  --allow-root --NotebookApp.token='' --NotebookApp.password=''