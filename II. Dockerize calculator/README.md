# Task II – Dockerize calculator.py

## Descriere
Am folosit aplicația Flask `calculator.py` și am containerizat-o cu Docker, apoi am automatizat procesul de build & push cu GitHub Actions.

## Pași realizați
- Am creat fișierele `Dockerfile` și `requirements.txt`
- Am folosit Gunicorn pentru a expune aplicația pe portul 8080
- Am definit un workflow GitHub Actions pentru:
  - Build Docker image
  - Autentificare în DockerHub
  - Push automat cu tag pe hash-ul commitului

## Testare locală (opțional)
```bash
docker build -t calc .
docker run -p 8080:8080 calc

## Trigger GitHub Actions run
