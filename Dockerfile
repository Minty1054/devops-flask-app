# Lab 5 - containerise the Flask app

# Start from the official Python image (already has Python and pip)
FROM python:3.14-slim

# Folder inside the container where the app lives
WORKDIR /app

# Install the dependencies first, so Docker can cache this layer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code into the container
COPY hello.py .

# Flask serves on port 5000 by default
EXPOSE 5000

# Start Flask; 0.0.0.0 makes it reachable from outside the container
CMD ["flask", "--app", "hello", "run", "--host=0.0.0.0", "--port=5000"]
