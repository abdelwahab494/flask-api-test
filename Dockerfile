# Use the official Python image from DockerHub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements (you can make one or I'll help you generate it)
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose port 5000 (same as your app)
EXPOSE 5000

# Run the Flask app
CMD ["python", "flask_api.py"]
