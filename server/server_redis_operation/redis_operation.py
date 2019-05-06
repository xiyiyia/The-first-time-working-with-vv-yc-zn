#! /usr/bin/python

import redis
import server.server_redis_operation.server_redis_pb2 as server_redis_pb2
import operator as op


class RedisOperation:
    def __init__(self):
        self.r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=False)
        self.the_user_data = server_redis_pb2.User()

    # if exists return 1 else return 0
    def check_id_exists(self, id_1):
        return self.r.exists(id_1)

    # if return True , success
    def check_signup(self, id_1, psw_1):
        self.the_user_data.ParseFromString(self.r.get(id_1))
        return op.eq(psw_1, self.the_user_data.PSW)

    def user_login(self, id_1, psw_1):
        self.the_user_data.ID = id_1
        self.the_user_data.PSW = psw_1
        self.the_user_data.IP = '1'
        self.the_user_data.STD = 0
        self.r.set(id_1, self.the_user_data.SerializeToString())
        self.r.save()

    def std_signup(self, id_1, ip_1):
        self.the_user_data.ParseFromString(self.r.get(id_1))
        self.the_user_data.STD = 1
        self.the_user_data.IP = ip_1
        self.r.set(id_1, self.the_user_data.SerializeToString())
        # self.r.save()

    def check_std(self, id_1):
        self.the_user_data.ParseFromString(self.r.get(id_1))
        return self.the_user_data.STD, self.the_user_data.IP


'''
redis_operation1 = redis_operation()
redis_operation1.user_login('1024','1024')
redis_operation1.user_login('2012','2012')
redis_operation1.std_logup('1024','192.168.1.100')
redis_operation1.std_logup('2012','192.168.1.101')
'''

