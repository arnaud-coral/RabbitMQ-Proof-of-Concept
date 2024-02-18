
# RabbitMQ Proof of Concept 🐇📦

This project demonstrates a simple yet effective use of RabbitMQ for message queuing within a Dockerized environment. It includes a publisher that sends messages containing unique UUIDs and subscribers that receives and logs these messages.

## Features 🌟

- **RabbitMQ Container**: utilizes the official RabbitMQ image with management plugin.
- **Custom Publisher**: Python script that publishes messages with a unique UUIDv4 to RabbitMQ queues.
- **Custom Subscribers**: Python scripts that subscribes to their RabbitMQ queue and logs received messages.
- **Docker Compose Integration**: orchestrates the RabbitMQ server, publisher, and subscribers services with ease of deployment in mind.
- **Logging**: Both publisher and subscribers log their activities to files for troubleshooting and monitoring.

## Prerequisites 📋

Before you start, make sure you have Docker and Docker Compose installed on your system.

## Setup and Running 🚀

Follow these steps to get your RabbitMQ PoC running:

1. **Clone the Repository**



2. **Build and Start Services**

   Use Docker Compose to build and start the services:

   ```bash
   docker-compose up --build
   ```

3. **Access RabbitMQ Management Interface**

   Open a web browser and navigate to `http://localhost:15672` to access the RabbitMQ Management Interface. Use the default credentials:

   - **Username**: user
   - **Password**: password

4. **View Logs**

   Logs are stored in the `logs` directory within your project folder. Tail the logs to see the messages being published and consumed:

   ```bash
   tail -f logs/file.log
   ```

## Architecture 🏗️

This PoC includes the following components:

- **RabbitMQ Server**: manages message queues and delivers messages between the publisher and subscriber.
- **Publisher**: a Python application that generates messages with unique UUIDs and publishes them to RabbitMQ queues.
- **Subscribers**: Python applications that subscribes to their queues, receives messages, and logs them.

## Troubleshooting 🛠️

If you encounter issues, check the following:

- Ensure Docker and Docker Compose are correctly installed and running.
- Verify that the RabbitMQ service has started by checking the Docker Compose logs.
- Confirm that the `logs` directory permissions allow writing from Docker containers.

## License 📄

Built with ❤️ by Arnaud Coral © 2024. It's licensed under CC BY-NC-SA 4.0. Please refer to the license for permissions and restrictions.

## Acknowledgments 👏

- RabbitMQ Team for the fantastic message broker.
- Docker for simplifying the deployment.

Happy messaging! 📩