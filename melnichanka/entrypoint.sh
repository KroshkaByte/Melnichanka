#!/bin/bash

echo "Сборка статических файлов"
python3 manage.py collectstatic --noinput

echo "Миграция базы данных"
python3 manage.py migrate

echo "Запуск веб-сервера"
exec nginx -c /etc/nginx/nginx.conf

