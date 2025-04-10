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

# create new key
# r.set('myKeyTTL23232323232', 'secret data', exat=datetime.datetime(year=2025, month=5, day=15, hour=3))


# list
# r.lpush('myList', 'elem1', 'elem2')
# r.expire('myList', 3500)

# read list
# data = r.lrange('myList', 0, -1)
# print(data)

# dicts
# r.hset('user:1234564', mapping={'city': 'Odesa'})
# r.hset('user:1234564', mapping={'age': 26})
# r.expire('user:1234564:age', 300)

# get data
# data = r.get('myKey')
# print(data)


# delete data
# r.delete('myList')

# data = r.hgetall('user:1234564')
# print(data)

# r.incr('views', 6)
# print(r.get('views'))


# pub/sub
# pubsub = r.pubsub()
# pubsub.subscribe('news')
# pubsub.subscribe('weather')
# for message in pubsub.listen():
#     print(message)


