# ==============================================================================  
# File: Dockerfile (untuk API Database Flask + Supabase)  
# ==============================================================================

FROM python:3.11-slim

# Install OS dependencies (kalau perlu debugging/SSL)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements dulu
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy seluruh source code
COPY . .

# Expose port (gunakan 8000 karena Railway defaultnya 8000)
EXPOSE 8000

# Jalankan Gunicorn (untuk production server)
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app.app:app"]
