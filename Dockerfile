FROM python:3.8

WORKDIR /usr/local/work

COPY ./requirements.txt ./
COPY ./contents ./

RUN pip install -r ./requirements.txt

