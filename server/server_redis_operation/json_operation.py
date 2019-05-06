#! /usr/bin/python

import json
import os
import server.server_redis_operation.redis_operation as redis_operation


class JsonServer:
    def __init__(self):
        self.redis = redis_operation.RedisOperation()

    @staticmethod
    def login_json(id_1):
        os.mkdir("./user_json/"+id_1)
        with open("./server_redis_operation/user_json/"+id_1+"/"+id_1+".json", "w+") as f:
            json.dump({id_1: {'STD': 0, 'IP': '0'}}, f, indent=4)
        f.close()

    @staticmethod
    def add_friend_json(send_1, receive_1):
        with open("./server_redis_operation/user_json/"+send_1+"/"+send_1+".json", 'r') as f:
            # print("Load str file from {}".format(str_file))
            str1 = f.read()
            r = json.loads(str1)
            # r[send_1]['count'] += 1
        f.close()
        with open("./server_redis_operation/user_json/" + send_1 + "/" + send_1 + ".json", 'w+') as f:
            r[receive_1] = {}
            r[receive_1]['STD'] = 0
            r[receive_1]['IP'] = '0'
            json.dump(r, f, indent=4, ensure_ascii=False)
        f.close()
        with open("./server_redis_operation/user_json/"+receive_1+"/"+receive_1+".json", 'r') as f:
            str1 = f.read()
            s = json.loads(str1)
        f.close()
        with open("./server_redis_operation/user_json/" + receive_1 + "/" + receive_1 + ".json", 'w+') as f:
            s[send_1] = {}
            s[send_1]['STD'] = 0
            s[send_1]['IP'] = '0'
            json.dump(r, f, indent=4, ensure_ascii=False)
        f.close()

    @staticmethod
    def del_friend_json(send_1, receive_1):
        with open("./server_redis_operation/user_json/" + send_1 + "/" + send_1 + ".json", 'r') as f:
            # print("Load str file from {}".format(str_file))
            str1 = f.read()
            r = json.loads(str1)
            # r[send_1]['count'] += 1
        f.close()
        with open("./server_redis_operation/user_json/" + send_1 + "/" + send_1 + ".json", 'w+') as f:
            del r[receive_1]
            json.dump(r, f, indent=4, ensure_ascii=False)
        f.close()
        with open("./server_redis_operation/user_json/" + receive_1 + "/" + receive_1 + ".json", 'r') as f:
            str1 = f.read()
            s = json.loads(str1)
        f.close()
        with open("./server_redis_operation/user_json/" + receive_1 + "/" + receive_1 + ".json", 'w+') as f:
            del s[send_1]
            json.dump(s, f, indent=4, ensure_ascii=False)
        f.close()

    def update_json(self, id_1):
        # os.path.normpath()
        file_path =  "./server_redis_operation/user_json/"+id_1+"/"+id_1+".json"
        with open(file_path, 'r') as f:
            str1 = f.read()
            r = json.loads(str1)
        f.close()

        key_user = r.keys()
        print(key_user)
        for i in key_user:
            satiation_1, ip_1 = self.redis.check_std(id_1)
            print(satiation_1, ip_1)
            if satiation_1 == 1 and r[i]['STD'] == 0:
                r[i]['STD'] = 1
                r[i]['IP'] = ip_1
        with open("./server_redis_operation/user_json/"+id_1+"/"+id_1+".json", 'w+') as f:
            json.dump(r, f, indent=4, ensure_ascii=False)
        f.close()

    def send_json(selfself, filename_sj):
        with open("./server_redis_operation/user_json/" + filename_sj + "/" + filename_sj + ".json", 'r') as f:
            event_msg = f.read()
            msg = json.loads(event_msg)
        f.close()
        # print(json_str)
        # print(event_msg)
        return repr(msg)


'''
json_server1 = json_server()
#json_server1.login_json('1024')
#json_server1.login_json('2012')
#json_server1.add_friend_json('2012','1024')
json_server1.update_json('1024')
json_server1.update_json('2012')
'''

