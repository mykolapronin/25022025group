import json

import pika.adapters.blocking_connection

from config import get_connection
from time import sleep


def produce_logs(channel: pika.adapters.blocking_connection.BlockingChannel):
    QUEUE = 'logs'
    # queue = channel.queue_declare(queue=QUEUE)

    for item in range(101):
        message = {"new_log": "user_registered", "user_id": item}
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE,
            body=json.dumps(message)
        )


# def produce_message(channel: pika.adapters.blocking_connection.BlockingChannel):
#     QUEUE='news'
#     queue = channel.queue_declare(queue=QUEUE)
#     message = 'hello kitty ))) {item}'
#     for item in range(10000):
#         channel.basic_publish(
#             exchange='',
#             routing_key=QUEUE,
#             body=message.format(item=item)
#         )


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            produce_logs(channel)


if __name__ == "__main__":
    main()
