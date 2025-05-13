FROM python:3.11.9-bookworm

# Set working directory
WORKDIR /app

# Copy app files
COPY . /app

# ✅ Install required system libraries for OpenCV
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

# Install Python dependencies
RUN pip install  -r requirements.txt

EXPOSE 8080
#here i added this insted of app.py
RUN python main.py  


# Run the application
CMD ["python3", "app.py"]
