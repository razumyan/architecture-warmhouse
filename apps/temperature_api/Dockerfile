# Runtime stage
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install necessary runtime dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY ./app /app

# Expose port 8081
EXPOSE 8081

# Sensor configuration
ENV SENSOR_IDS=1,2
ENV SENSOR_LOCATIONS_1="Area 1"
ENV SENSOR_LOCATIONS_2="Area 2"

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081", "--reload"]
