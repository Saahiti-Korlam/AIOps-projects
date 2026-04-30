# Use official Python base image
FROM python:3.9-slim-buster AS builder

# Set workin directory to /app
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Compile and package the application
RUN python setup.py sdist bdist_wheel

# Create a new image with the packaged app
FROM python:3.9-slim-buster

# Set workin directory to /app
WORKDIR /app

# Move the packaged wheel into the container's filesystem
COPY --from=builder dist/* .

# Expose port 8000 for Flask or similar
EXPOSE 8000

# Run command to start the application
CMD ["python", "main.py"]
