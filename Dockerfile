FROM python:3.9-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set default environment variables
ENV SESSION_NAME=TGVCMusic
ENV DOWNLOAD_PATH=/app/downloads
ENV DURATION_LIMIT=10

# Run the setup script if no config is provided
CMD ["sh", "-c", "if [ ! -f config.json ] && [ -z \"$API_ID\" ]; then python setup.py; fi && python main.py"]