FROM python:3.9-alpine

ADD . /app
WORKDIR /app

RUN pip install -r requirements

EXPOSE 8000
CMD python /app/exporter.py
