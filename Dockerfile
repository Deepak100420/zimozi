# Use official Python image
FROM python:3.13

# Set the working directory
WORKDIR /app

# Copy the FastAPI app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn

# Expose port 8000
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
