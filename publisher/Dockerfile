FROM python:3.9-slim
WORKDIR /app
COPY publisher.py .
RUN pip install pika
CMD ["python", "./publisher.py"]
