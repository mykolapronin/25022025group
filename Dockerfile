FROM python:3.11-alpine

WORKDIR /app

COPY main.py /app

ENTRYPOINT ["python", "main.py"]
