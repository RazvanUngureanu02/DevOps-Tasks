# Use a lightweight official Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy application files into the container
COPY calculator.py /app/
COPY requirements.txt /app/

# Install all dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define a default environment variable for the port
ENV APP_PORT=8080

# Expose port 8080 to allow external access
EXPOSE 8080

# Start the Flask application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "calculator:app"]
