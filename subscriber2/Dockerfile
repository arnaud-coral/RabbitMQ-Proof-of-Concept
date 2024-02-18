FROM python:3.9-slim
WORKDIR /app
COPY subscriber2.py .
RUN pip install pika
CMD ["python", "./subscriber2.py"]
