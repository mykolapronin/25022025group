import time

from config import get_connection
import pika

import json


def process_new_message(channel, method, properties, body):
    message = json.loads(body)
    print(f"New log: {message['new_log']}, user_id: {message['user_id']}")
    time.sleep(1)
    channel.basic_ack(delivery_tag=method.delivery_tag)


def consume_logs(channel: pika.adapters.blocking_connection.BlockingChannel):
    QUEUE = 'logs'
    channel.queue_declare(queue=QUEUE)
    channel.basic_consume(
        queue=QUEUE,
        on_message_callback=process_new_message,
        # auto_ack=True
    )
    channel.start_consuming()


# def consume_logs(channel: pika.adapters.blocking_connection.BlockingChannel):
#     QUEUE = 'news'
#     channel.basic_consume(
#         queue=QUEUE,
#         on_message_callback=process_new_message,
#         # auto_ack=True
#     )
#
#     channel.start_consuming()


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            consume_logs(channel)


if __name__ == "__main__":
    main()
