# Stage 1: Build Environment
FROM python:3.11-slim AS build-env

# # Create the virtualenv inside the project’s root directory.
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

# Set working directory
WORKDIR /app

# Copy the entire project
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip && pip install poetry

RUN poetry install

CMD ["./run.sh"]