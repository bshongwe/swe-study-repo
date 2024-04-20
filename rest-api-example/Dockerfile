# Use the official Python image
FROM python:3.9-slim

# Set environment variables to prevent Python from writing pyc files
# and buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy requirements file into container at /src
COPY requirements.txt .

# Install dependencies listed in requirements.txt using pip
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container at /src
COPY . .

# Expose the port that the Flask app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "run.py"]

