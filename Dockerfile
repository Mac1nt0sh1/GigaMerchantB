FROM python:3.11

WORKDIR /app

# Copy dependency files from project root
COPY ../pyproject.toml ../poetry.lock* ./

# Install Poetry and dependencies
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

# Copy current folder (src)
COPY . ./src/

WORKDIR /app/src

# Run the application
CMD ["python", "-m", "bot"]
