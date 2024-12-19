FROM python:3.13-bookworm

RUN apt-get update && apt-get install -y graphviz

COPY requirements.txt /requirements.txt
COPY entrypoint.py /entrypoint.py

RUN pip install -r requirements.txt

ENTRYPOINT ["/entrypoint.py"]
