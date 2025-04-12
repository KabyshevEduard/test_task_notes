#!/bin/bash

docker compose --env-file ./notes/notes/.env up -d --build
docker compose exec drf python3 manage.py migrate
docker compose exec drf python3 manage.py makemigrations api
docker compose exec drf python3 manage.py migrate
