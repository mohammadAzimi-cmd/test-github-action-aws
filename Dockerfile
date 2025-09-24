FROM python:3.8-alpine

WORKDIR /app

COPY script.py .

CMD ["python", "script.py"]