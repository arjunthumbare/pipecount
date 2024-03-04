FROM python:3.8.15-slim-bullseye

USER root

RUN apt-get update

RUN mkdir pipecount
WORKDIR pipecount

COPY . .

RUN python3 -m pip install -r requirements.txt

EXPOSE 80

CMD  ["python3","-m","streamlit","run","pipecount.py", "--server.port=80","--server.address=0.0.0.0","--theme.base=light"]
