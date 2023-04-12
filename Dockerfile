FROM python:3.11-alpine
RUN apk add --update --no-cache supervisor
RUN apk add --no-cache tzdata
ENV TZ=Europe/London
WORKDIR /flask
COPY app app
COPY supervisor_apps.ini supervisor_apps.ini
COPY supervisord.conf supervisord.conf
COPY gunicorn.conf.py gunicorn.conf.py
COPY requirements.txt requirements.txt
RUN python3 -m venv venv
RUN venv/bin/pip install -r requirements.txt
CMD ["venv/bin/supervisord", "-c", "supervisord.conf"]