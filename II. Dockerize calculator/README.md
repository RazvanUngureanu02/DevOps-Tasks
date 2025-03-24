# Dockerized Calculator – Task II

This folder contains a complete Python web application containerized with Docker, as part of Task II in the DevOps Internship 2025 project.

## Contents

- `calculator.py` – The main Flask application
- `requirements.txt` – Python dependencies
- `Dockerfile` – Instructions to build the Docker image
- `.github/workflows/docker-image.yml` – GitHub Actions workflow for build & push automation
- `README.md` – This documentation file

---

## Application Features

- Built with Python and Flask
- Supports two operations via API: **addition** and **multiplication**
- Web interface included (HTML + JavaScript)
- Exposed on port **8080**
- Graceful shutdown on `SIGINT` and `SIGTERM`
- Configurable port using `APP_PORT` environment variable

---

## How to Use

### 1. Pull Image from Docker Hub

```bash
docker pull alexandruungureanu/calculator:<commit_hash>

## Run Container
docker run -p 8080:8080 alexandruungureanu/calculator:<commit_hash>

## Then open in browser:
http://localhost:8080

## API Endpoints
POST /calculate
Request Body (JSON):

json
{
  "operation": "add",
  "numbers": [1, 2, 3]
}
Response:

json
{
  "result": 6
}

GET /
Returns a web interface for calculator operations.

## Manual Build (Optional)
To test locally without pulling from Docker Hub:

docker build -t calculator .
docker run -p 8080:8080 calculator

GitHub Actions Automation
GitHub Actions CI/CD pipeline is configured to:

Trigger on push to the main branch

Build the Docker image using the Dockerfile

Tag the image using the current commit hash

Push the image to Docker Hub: alexandruungureanu/calculator

Workflow file location:
.github/workflows/docker-image.yml

## Dockerfile Summary
FROM python:3.10-slim
WORKDIR /app
COPY calculator.py /app/
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
ENV APP_PORT=8080
EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "calculator:app"]

Bonus Features
Graceful Shutdown
The app uses Python’s signal module to handle container termination events (SIGINT, SIGTERM).

Environment Variables
The port is configurable using:
ENV APP_PORT=8080
