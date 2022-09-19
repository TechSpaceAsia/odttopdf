from python:3.10-slim-buster

RUN mkdir /code
RUN apt update && apt install -y libreoffice
RUN pip install --upgrade pip && pip install celery redis

WORKDIR /code
COPY celeryconfig.py worker ./

CMD celery -A worker worker -l DEBUG

