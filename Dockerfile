FROM python:3.12

ENV DJANGO_SETTINGS_MODULE=melnichanka.settings

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip \
 && pip install -r requirements.txt

COPY melnichanka /app/melnichanka

CMD ["python3", "melnichanka/manage.py", "runserver", "0.0.0.0:8000"]
