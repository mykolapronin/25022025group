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

# Firstly

# r.set('myKeyFavCar', 'nissan gtr 34')
# r.set('myLovelyPet', 'Dog named Sam(i miss you)')
# r.expire('myLovelyPet', 7200)
r.lpush('listOfProducts', 'coffee', 'tea')


