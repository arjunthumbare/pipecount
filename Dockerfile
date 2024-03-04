# FROM python:3.8.15-slim-bullseye

# USER root

# RUN apt-get update

# RUN mkdir pipecount
# WORKDIR pipecount

# COPY . .

# RUN python3 -m pip install -r requirements.txt

# EXPOSE 80

# CMD  ["python3","-m","streamlit","run","pipecount.py", "--server.port=80","--server.address=0.0.0.0","--theme.base=light"]


 
FROM python:3.8.15-slim-bullseye
ENV DEBIAN_FRONTEND noninteractive
RUN apt update
RUN TZ=Etc/UTC apt install -y tzdata
RUN apt install --no-install-recommends -y gcc git zip curl htop libgl1-mesa-glx libglib2.0-0 libpython3-dev gnupg g++
RUN apt upgrade --no-install-recommends -y openssl tar
USER root
 
RUN apt-get update
 
RUN mkdir pipecount
WORKDIR pipecount
 
COPY . .
 
RUN python3 -m pip install -r requirements.txt
 
EXPOSE 80
 
CMD  ["python3","-m","streamlit","run","pipecount.py", "--server.port=80","--server.address=0.0.0.0","--theme.base=light"]