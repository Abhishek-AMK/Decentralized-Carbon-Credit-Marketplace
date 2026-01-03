# Process 1: Build Frontend
FROM node:20 as frontend-build
WORKDIR /app
COPY marketplace_app /app
RUN npm install
RUN npx reflex export --frontend-only

# Process 2: Python Backend
FROM python:3.12-slim
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

# Expose ports
EXPOSE 8080

# Command to run Reflex in production
CMD ["sh", "-c", "cd marketplace_app && reflex run --env production --frontend-port 8080 --backend-port 8000"]
