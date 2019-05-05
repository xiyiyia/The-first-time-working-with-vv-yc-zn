#! /usr/bin/python

import redis
import AS_redis_operation.AS_redis_pb2 as AS_redis_pb2


class RedisOperation:
    def __init__(self):
        self.r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=False)
        self.the_user_data = AS_redis_pb2.User_AI()

    # return key c and key tgs (key c\tgs and key c\v random to get)
    def ip_key(self, id_1):
        self.the_user_data = self.r.get(id_1)
        return self.the_user_data.Key_op, self.the_user_data.Key_tgs
