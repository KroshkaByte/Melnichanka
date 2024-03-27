FROM python:3.12-alpine3.18

WORKDIR /app

ENV DJANGO_SETTINGS_MODULE=melnichanka.settings
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/

RUN pip install --upgrade pip \
 && pip install -r requirements.txt

COPY . .
