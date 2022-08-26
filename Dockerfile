FROM python:3.10.2-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install curl -y \
    && apt-get -y install libpq-dev gcc \
    && curl -sSL https://install.python-poetry.org | python - --version 1.1.14

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /opt/bender

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir setuptools wheel \
    && pip install --no-cache-dir poetry

RUN poetry install --no-dev

COPY . .

CMD ["poetry", "run", "python", "-m", "bot"]
