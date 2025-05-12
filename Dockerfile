FROM python:3.11.9-bookworm

# Set working directory
WORKDIR /app

# Copy app files
COPY . /app

# ✅ Install required system libraries for OpenCV
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for App Runner
EXPOSE 8080

# Run the application
CMD ["python3", "app.py"]
