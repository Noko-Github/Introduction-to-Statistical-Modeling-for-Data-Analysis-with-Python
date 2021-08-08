FROM python:3.8

WORKDIR /usr/local/work

COPY ./* ./

RUN pip install -r ./requirement.txt

