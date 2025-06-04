# Use official Python image
FROM python:3.10-slim

# Set work directory inside container
WORKDIR /app

# Copy local files into container
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Set the default command
CMD ["python", "app.py"]
