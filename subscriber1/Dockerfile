FROM python:3.9-slim
WORKDIR /app
COPY subscriber1.py .
RUN pip install pika
CMD ["python", "./subscriber1.py"]
