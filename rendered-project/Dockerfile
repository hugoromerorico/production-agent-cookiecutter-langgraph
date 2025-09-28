ARG image=python:3.13-slim-bookworm

FROM ${image}

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --locked --no-install-project

COPY ./app ./app

RUN uv sync --locked
EXPOSE 8080

CMD ["uv", "run", "fastapi", "run", "app/main.py", "--port=8080", "--host=0.0.0.0"]
