FROM python:3.12.2-slim

WORKDIR /app

ENV DJANGO_SETTINGS_MODULE=melnichanka.settings
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/

RUN apt-get clean && apt-get update && apt-get install -y locales
RUN locale-gen ru_RU.UTF-8

RUN pip install --upgrade pip \
 && pip install -r requirements.txt

COPY . .
