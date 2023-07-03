FROM python:3.9-slim

WORKDIR /audio_converter_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /audio_converter_app/docker/*.sh
