#!/bin/bash

echo "Сборка статических файлов"
python3 manage.py collectstatic --noinput

echo "Создание миграций"
python3 manage.py makemigrations

echo "Миграция базы данных"
python3 manage.py migrate

echo "Запуск nginx"
exec nginx -c /etc/nginx/nginx.conf

echo "Запуск gunicorn"
exec gunicorn melnichanka.wsgi:application --config gunicorn.conf.py --bind 0.0.0.0:8000
