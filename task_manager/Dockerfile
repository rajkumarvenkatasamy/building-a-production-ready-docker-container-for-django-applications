# Comment: Dockerfile for the task_manager project - starts
# # Stage 1: Build Environment
# FROM python:3.11-slim AS build-env

# # Set environment variables
# # This prevents Python from writing out pyc files
# ENV PYTHONDONTWRITEBYTECODE=1
# # This keeps Python from buffering stdin/stdout
# ENV PYTHONUNBUFFERED=1
# # Create the virtualenv inside the project’s root directory.
# ENV POETRY_VIRTUALENVS_IN_PROJECT=true

# # Install dependencies
# RUN pip install --upgrade pip
# RUN pip install poetry

# # Set working directory
# WORKDIR /app

# # Copy project files
# COPY pyproject.toml poetry.lock /app/
# RUN poetry install --no-dev

# # Copy the entire project
# COPY . /app/

# # Stage 2: Runtime Environment
# FROM gcr.io/distroless/python3

# # Set working directory
# WORKDIR /app

# # Copy files from build environment
# COPY --from=build-env /app /app

# # RUN chmod +x run.sh

# # Expose port 8000
# EXPOSE 8000

# # Command to run the application
# CMD ["./run.sh"]

# Comment: Dockerfile for the task_manager project - ends

FROM python:3.11-slim AS build-env

# Set the working directory
WORKDIR /app

# Copy the project directory to the working directory
RUN pip install poetry 

COPY . .

RUN poetry config virtualenvs.create true \
    && poetry install --no-dev

RUN chmod +x run.sh

# Specify the command to run on container start
CMD ["./run.sh"]
