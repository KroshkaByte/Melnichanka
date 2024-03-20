FROM python:3.12-slim

ENV DJANGO_SETTINGS_MODULE=melnichanka.settings

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip \
 && pip install -r requirements.txt

COPY . .
