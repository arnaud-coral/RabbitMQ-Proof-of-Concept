
import pika
import time
import logging

logging.basicConfig(filename='/app/logs/file.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def callback(ch, method, properties, body):
    message = body.decode()
    logging.info(f"Received {message}")

def start_consuming():
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitmq', credentials=pika.PlainCredentials('user', 'password')))
        channel = connection.channel()

        channel.queue_declare(queue='subscriber2')

        channel.basic_consume(queue='subscriber2',
                              on_message_callback=callback,
                              auto_ack=True)

        logging.info('Subscriber2 waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
    except Exception as e:
        logging.error(f"Error in subscriber2: {e}")
    finally:
        if connection:
            connection.close()
            logging.info("Subscriber2 connection closed")

if __name__ == '__main__':
    logging.info("Subscriber2 started")
    start_consuming()
