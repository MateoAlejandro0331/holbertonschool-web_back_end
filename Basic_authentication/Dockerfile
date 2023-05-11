# Set the base image
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY api api
COPY models models

# Set the environment variable
ENV FLASK_APP=api/app.py

# Expose the port
EXPOSE 5000

# Start the application
CMD ["flask", "run", "--host=0.0.0.0"]