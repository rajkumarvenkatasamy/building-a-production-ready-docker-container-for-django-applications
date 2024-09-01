FROM python:3.11-slim

# # Create the virtualenv inside the project’s root directory.
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

# Set working directory
WORKDIR /app

# Copy the dependency requirements files
COPY pyproject.toml poetry.lock /app/

# Install dependencies
RUN pip install --upgrade pip && pip install poetry

RUN poetry install --no-root

# Copy the entire project
COPY . /app/

# set PYTHONPATH
ENV PYTHONPATH=/app:/app/.venv/bin:
ENV PATH=/app:/app/.venv/bin:$PATH

# Start the app
CMD ["sh", "./run.sh"]