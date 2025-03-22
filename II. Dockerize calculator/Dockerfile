# Folosește imaginea de bază Python slim pentru un container lightweight
FROM python:3.10-slim

# Setează directorul de lucru din container
WORKDIR /app

# Copiază fișierele aplicației în container
COPY calculator.py /app/
COPY requirements.txt /app/

# Instalează toate dependențele specificate în requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Setează o variabilă de mediu pentru port (poate fi modificată ușor)
ENV APP_PORT=8080

# Expune portul 8080 către exterior (portul pe care va rula gunicorn)
EXPOSE 8080

# Comandă de rulare a aplicației Flask folosind gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "calculator:app"]
