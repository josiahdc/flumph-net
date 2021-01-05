import redis


class RedisConnection:
    def __init__(self):
        pool = redis.ConnectionPool(host="localhost", port=6379, db=0)