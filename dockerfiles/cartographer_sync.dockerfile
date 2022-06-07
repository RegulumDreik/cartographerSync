FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ARG POETRY_VIRTUALENVS_CREATE=false

RUN pip install pip && \
    pip install poetry==1.1.13

WORKDIR /app/
COPY ./ /app/

RUN poetry install --no-dev --ansi
