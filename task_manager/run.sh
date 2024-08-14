#!/bin/bash

poetry run python manage.py makemigrations
poetry run python manage.py migrate
poetry run python manage.py collectstatic --noinput
poetry run uvicorn task_manager.asgi:application --host 0.0.0.0 --port 8000