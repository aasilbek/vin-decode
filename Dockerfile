# Pull base image

FROM python:3.8.5-slim

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
# Set some env varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY /requirements /app
RUN pip install --upgrade pip && pip install -r /app/development.txt

COPY src /app