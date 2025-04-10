#!/bin/bash

docker compose up -d --build
docker compose exec drf python3 manage.py migrate
docker compose exec drf python3 manage.py makemigrations api
docker compose exec drf python3 manage.py migrate