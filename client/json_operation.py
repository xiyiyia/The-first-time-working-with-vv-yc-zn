#! /usr/bin/python

import json
import os
import operator as op


class JsonServer:
    def __init__(self, id_1):
        self.ID = id_1

    def user_signup(self):
        os.mkdir("./user_json/"+self.ID)

    @staticmethod
    def add_friend_json(send_1, receive_1, receive_ip):
        with open("./user_json/"+send_1+"/"+send_1+".json", 'r') as f:
            # print("Load str file from {}".format(str_file))
            str1 = f.read()
            r = json.loads(str1)
            # r[send_1]['count'] += 1
        f.close()
        with open("./user_json/" + send_1 + "/" + send_1 + ".json", 'w+') as f:
            r[receive_1] = {}
            r[receive_1]['STD'] = 1
            r[receive_1]['IP'] = receive_ip
            json.dump(r, f, indent=4, ensure_ascii=False)
        f.close()
    @staticmethod
    def del_friend_json(send_1, receive_1):
        with open("./user_json/" + send_1 + "/" + send_1 + ".json", 'r') as f:
            # print("Load str file from {}".format(str_file))
            str1 = f.read()
            r = json.loads(str1)
            # r[send_1]['count'] += 1
        f.close()
        with open("./user_json/" + send_1 + "/" + send_1 + ".json", 'w+') as f:
            del r[receive_1]
            json.dump(r, f, indent=4, ensure_ascii=False)
        f.close()

    def friend_list(self, ID_1):
        with open("./user_json/"+ID_1+"/"+ID_1+".json", "r") as f:
            str1 = f.read()
            r = json.loads(str1)
        f.close()
        return r

    def friend_ip(self,ip_1):
        with open("./user_json/"+self.ID+"/"+self.ID+".json", "r") as f:
            str1 = f.read()
            r = json.loads(str1)
        f.close()
        key_user = r.keys()
        for i in key_user:
            if op.eq(i, ip_1):
                return r[i]['IP']
    def UpdateJson(self, filename_UJ, data_UJ):
        with open("./user_json/"+filename_UJ+"/"+filename_UJ+".json", 'w+') as f:
            f.write(data_UJ)
        f.close()
    def CreateJson(self, filename_UJ, data_UJ):
        os.mkdir("./user_json/"+data_UJ)
        with open("./user_json/"+filename_UJ+"/"+filename_UJ+".json", 'w+') as f:
            f.write(data_UJ)
        f.close()

'''
json_server1 = json_server()
#json_server1.login_json('1024')
#json_server1.login_json('2012')
#json_server1.add_friend_json('2012','1024')
json_server1.update_json('1024')
json_server1.update_json('2012')
'''

