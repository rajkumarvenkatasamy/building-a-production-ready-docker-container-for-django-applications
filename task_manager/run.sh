#!/bin/bash

poetry run uvicorn task_manager.asgi:application --host 0.0.0.0 --port 8000