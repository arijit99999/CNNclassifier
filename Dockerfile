FROM python:3.11.9-bookworm

# Set working directory
WORKDIR /app

# Install required system libraries for OpenCV and DVC support
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    git \
    curl \
    && apt-get clean

# Copy project files including DVC, Git, and data configs
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ✅ Install DVC (core only, or use dvc[s3] if needed)
RUN pip install dvc

# ✅ Configure Git (DVC requires this)
RUN git config --global user.name "arijit" \
    && git config --global user.email "arijitdey289@gmail.com"

# ✅ Run DVC pull and repro
RUN dvc pull || (echo "❌ DVC pull failed. Check credentials or remote config." && exit 1)
RUN dvc repro || (echo "❌ DVC repro failed. Check pipeline or dependencies." && exit 1)

# Expose app port
EXPOSE 8080

# Start Flask app
CMD ["python3", "app.py"]
