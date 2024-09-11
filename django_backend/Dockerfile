# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY django_backend/ /app/

# Install pip and any needed packages specified in requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=myproject.settings

# Run Django server when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "document_management.wsgi:application"]
