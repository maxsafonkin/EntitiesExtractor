FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN python3.11 -m pip install -r /app/requirements.txt

COPY src /app/src

CMD ["python3.11", "/app/src/start.py"]