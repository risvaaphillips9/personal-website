# Python slim image for a small runtime
FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    FLASK_APP=app:app \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=5000

WORKDIR /app

# System deps (if needed later). Keeping minimal for now.
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
#  && rm -rf /var/lib/apt/lists/*

# Install Python dependencies first for better layer caching
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Ensure expected folders exist (images saved here)
RUN mkdir -p static/images

# Expose Flask port
EXPOSE 5000

# Start the Flask development server (sufficient for this app). For production,
# consider adding gunicorn to requirements and using it instead.
CMD ["flask", "run"]

