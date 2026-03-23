# 1. Use an official lightweight Python image
FROM python:3.10-slim

# 2. Set environment variables to ensure Python output is logged properly
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Create a directory for your app code
WORKDIR /app

# 4. Install system dependencies needed for the Neon/Postgres database
# We need 'libpq-dev' and 'gcc' to install the database driver (psycopg2)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 5. Copy the requirements file first (this speeds up future builds)
COPY requirements.txt .

# 6. Install your Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# 7. Copy all your backend code into the /app folder
COPY . .

# 8. Start the app using Gunicorn
# 'app:app' means look in 'app.py' for the object named 'app'
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 "app:create_app()"