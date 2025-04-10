FROM python:3.10.12-alpine

WORKDIR /usr/src/app

COPY reqs.txt .
COPY notes .

RUN pip install --no-cache-dir -r reqs.txt





