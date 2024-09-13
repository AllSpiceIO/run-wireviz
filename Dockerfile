FROM python:3.11-slim

RUN apt-get update && apt-get install -y graphviz

COPY requirements.txt /requirements.txt
COPY entrypoint.py /entrypoint.py

RUN pip install -r requirements.txt

ENTRYPOINT ["/entrypoint.py"]
