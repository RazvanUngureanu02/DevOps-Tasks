FROM python:3.10-slim

WORKDIR /app

COPY calculator.py /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "calculator:app"]
