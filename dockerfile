# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install tstl and other dependencies
RUN pip install --no-cache-dir tstl

# Expose port (optional, if your app is a web app)
EXPOSE 5000

# Run the Python script when the container starts
CMD ["python", "vehicle_management.py"]
