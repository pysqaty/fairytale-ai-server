# syntax=docker/dockerfile:1

FROM python:3.11

EXPOSE 8000

WORKDIR /fairytale_ai_server

ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PYTHONUNBUFFERED=true \
    PATH="/root/.local/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 -
COPY ./pyproject.toml ./poetry.lock ./README.md ./

RUN poetry install --no-root --without dev --sync --no-ansi --no-interaction

COPY ./fairytale_ai_server /fairytale_ai_server

RUN apt-get update && apt-get install -y dos2unix && apt-get -y clean
RUN chmod +x entrypoint.sh
RUN dos2unix entrypoint.sh

CMD ["./entrypoint.sh", "uvicorn", "fairytale_ai_server.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--lifespan", "off"]
