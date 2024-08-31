# Stage 1: Build Environment
FROM python:3.11-slim AS build-env

# # Create the virtualenv inside the project’s root directory.
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml poetry.lock /app/

# Install dependencies
RUN pip install --upgrade pip && pip install poetry

RUN poetry install --no-root

# Copy the entire project
COPY . /app/

# Stage 2: Runtime Environment
FROM gcr.io/distroless/python3

# Set environment variables
# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app
# Copy files from build environment
COPY --from=build-env /app /app
# COPY --from=build-env /app/.venv/bin/uvicorn /app/uvicorn

# set PYTHONPATH
ENV PYTHONPATH=/app:/app/.venv/bin:/app/.venv/lib/python3.11/site-packages/
ENV PATH=/app:/app/.venv/bin:/app/.venv/lib/python3.11/site-packages/:$PATH

# Expose port 8000
EXPOSE 8000

# Start the application
CMD ["entrypoint.py"]
