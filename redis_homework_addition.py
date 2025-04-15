"""Basic connection example.
"""

import redis
import datetime

r = redis.Redis(
    host='redis-13513.c273.us-east-1-2.ec2.redns.redis-cloud.com',
    port=13513,
    decode_responses=True,
    username="default",
    password="mu00BOpNWHKd6X8I65uXTIY7hhLOq3v8",
)

pubsub = r.pubsub()
pubsub.subscribe('school')

with open('math_test.txt', 'a', encoding='utf-8') as file:
    for message in pubsub.listen():
        text = str(message['data'])

        if 'контрольна робота' in text.lower():
            file.write(f'{text} is on the way \n')
