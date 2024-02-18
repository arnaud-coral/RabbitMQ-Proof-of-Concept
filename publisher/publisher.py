import pika
import time
import logging
import uuid

logging.basicConfig(filename='/app/logs/file.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def publish_message():
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitmq', credentials=pika.PlainCredentials('user', 'password')))
        channel = connection.channel()

        channel.queue_declare(queue='subscriber1')

        while True:
            message_uuid = uuid.uuid4()
            message = f'message for subscriber1: {message_uuid}'
            channel.basic_publish(exchange='',
                                  routing_key='subscriber1',
                                  body=message)
            logging.info(f"Sent {message}")

            message_uuid = uuid.uuid4()
            message = f'message for subscriber2: {message_uuid}'
            channel.basic_publish(exchange='',
                                  routing_key='subscriber2',
                                  body=message)
            logging.info(f"Sent {message}")

            time.sleep(2)
    except Exception as e:
        logging.error(f"Error in publisher: {e}")
    finally:
        if connection:
            connection.close()
            logging.info("Publisher connection closed")

if __name__ == '__main__':
    logging.info("Publisher started")
    publish_message()
