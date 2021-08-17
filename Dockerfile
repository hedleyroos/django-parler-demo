# syntax = docker/dockerfile:experimental
FROM python:3.7.11-buster
WORKDIR /var/app

#RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y vim

COPY requirements.txt /var/app/
COPY manage.py /var/app/
COPY wsgi.py /var/app/
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip python -m pip install -r /var/app/requirements.txt
COPY sample.sqlite3 /var/app/db.sqlite3
COPY parlerdemo /var/app/parlerdemo
ADD media /var/app/media/

EXPOSE 80
ENTRYPOINT python manage.py runserver 0.0.0.0:80 --noreload
