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
# Now list

# r.lpush('myList', 'coffee', 'tea')
# exp_at = datetime.datetime(year=2025, month=4, day=19, hour=3)
# r.expireat('myList', exp_at)

# Now dictionary

# r.hset('products_for_cake', mapping={"flour": 250, "milk": 500})
# r.hset('products_for_cake', mapping={"sugar": 500})

# r.delete('products_for_cake')


# SUBSCRIBE

# pubsub = r.pubsub()
# r.publish('school', 'контрольна робота')
# r.publish('school', 'робота')
# r.publish('school', 'неробота')



