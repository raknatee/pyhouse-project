FROM tensorflow/tensorflow:2.6.0


RUN apt update -y && apt upgrade -y
ENV DEBIAN_FRONTEND="noninteractive"

RUN apt install -yfm --no-install-recommends libgl1-mesa-glx libgtk2.0-dev

RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa


RUN apt install python3.10 -y
RUN apt install python3-pip -y
RUN apt install python3.10-distutils -y
RUN pip3 install pipenv

RUN pipenv --python 3.10


WORKDIR /home/container
RUN mkdir .venv

RUN pipenv install ipython==6.5.0
RUN pipenv install jupyterlab==3.4.4
RUN pipenv install torch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 
RUN pipenv install 'pillow' 
RUN pipenv install opencv-python==4.6.0.66 
RUN pipenv install "sklearn" 
RUN pipenv install "pandas" 
RUN pipenv install "seaborn" 
RUN pipenv install "matplotlib" 
RUN pipenv install "mypy==0.910" 
RUN pipenv install "pytest==6.2.5" 
RUN pipenv install "mne==0.23.4" 
RUN pipenv install "scipy==1.9.0" 
RUN pipenv install mypy 






# COPY ./jupyter_config /root/.jupyter
CMD tail -f /dev/null
# CMD pipenv run jupyter lab --ip='*' --port=8888 --no-browser  --allow-root --NotebookApp.token='' --NotebookApp.password=''