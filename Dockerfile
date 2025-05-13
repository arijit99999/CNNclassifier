FROM python:3.11.9-bookworm

WORKDIR /app

# Install OpenCV and system packages
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    git \
    curl

# Install Python requirements
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Configure Git (DVC needs Git)
RUN git config --global user.name "arijit" && git config --global user.email "arijitdey289@gmail.com"

# Run DVC pipeline during build
RUN dvc pull && dvc repro

EXPOSE 8080
CMD ["python3", "app.py"]
