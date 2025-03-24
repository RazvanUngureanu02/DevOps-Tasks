# DevOps Internship – Task II: Dockerized Calculator Application

## Overview

This project provides a containerized version of a simple web calculator application written in Python using the Flask framework. It performs basic arithmetic operations (addition and multiplication) through an interactive HTML interface and a RESTful API.

The application is packaged into a Docker container, tested locally, and pushed to Docker Hub using a CI/CD pipeline implemented with GitHub Actions.

---

## Project Structure

2-app/ ├── calculator.py # Flask web application ├── Dockerfile # Docker instructions to build the image ├── requirements.txt # Python dependencies └── .github/workflows/ └── docker-image.yml # GitHub Actions workflow for automation

yaml
Copy
Edit

---

## Steps Completed

### 1. Application Selection

The selected application is `calculator.py` located in the `2-app/` folder. It is a Python web application based on Flask. The dependencies are listed in the `requirements.txt` file.

---

### 2. Dockerfile Implementation

The Dockerfile was created to containerize the application with the following configuration:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY calculator.py /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

ENV APP_PORT=8080

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "calculator:app"]
Key points:

Lightweight image based on python:3.10-slim

Uses Gunicorn as a production WSGI server

Port configured using APP_PORT environment variable

Port 8080 is exposed for web access

3. Application Testing Locally
The image was pulled and tested using the following commands:

bash
Copy
Edit
docker pull alexandruungureanu/calculator:<tag>
docker run -p 8080:8080 alexandruungureanu/calculator:<tag>
After running, accessing http://localhost:8080 in the browser loads the calculator’s HTML interface.

4. DockerHub Repository Setup
Docker Hub account: alexandruungureanu

Public repository: calculator

Images are tagged using commit hashes and available for pull

5. GitHub Actions CI/CD Pipeline
A GitHub Actions workflow was configured to:

Trigger on push to main branch

Build the Docker image using the provided Dockerfile

Tag the image with the commit SHA

Push it automatically to Docker Hub

All automation is handled in .github/workflows/docker-image.yml.

Bonus Features
Graceful Shutdown
The application handles SIGTERM and SIGINT signals using Python’s signal module to exit cleanly when the container is stopped.

Environment Configuration
The port the application runs on is controlled via an environment variable:

dockerfile
Copy
Edit
ENV APP_PORT=8080
This makes it easy to override the port if necessary in deployment environments.

API Specification
POST /calculate
Accepts a JSON body:

json
Copy
Edit
{
  "operation": "add",
  "numbers": [1, 2, 3]
}
Responds with:

json
Copy
Edit
{
  "result": 6
}
GET /
Returns an HTML interface for interactive use.

Optional Manual Build and Run
For manual local testing without pulling from Docker Hub:

bash
Copy
Edit
docker build -t calculator .
docker run -p 8080:8080 calculator
Then open http://localhost:8080 in your browser.
