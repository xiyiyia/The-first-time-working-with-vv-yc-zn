import des_encryption as des_en
import Tstr as tostr
import redis
import time
import socket


def get_ticket(Key_ctgs, ip_Client, ip_TGS, ts2, lifetime2, r):
    # 在此要从数据库获取E_tgs，是TGS和AS之间使用的对称密钥
    Key_tgs = (r.get('Key_TGS')).decode()
    AD_c = ip_Client
    ticket = Key_ctgs + ip_Client + ip_Client + ip_TGS + ts2 + lifetime2
    ticket = des_en.test(ticket, Key_tgs)
    print("ticket = ", ticket)
    return ticket


def AS_to_Client(ip_Client, r):
    Key_c = (r.get('Key_Client')).decode()
    Key_c = tostr.key_tostr(Key_c)

    Key_ctgs = (r.get('Key_ctgs')).decode()  # 理论上从数据库获取
    Key_ctgs = tostr.key_tostr(Key_ctgs)
    print("Key_ctgs = ", Key_ctgs)

    ip_TGS = (r.get('ip_TGS')).decode()  # 从数据库获取TGS的IP地址
    ip_TGS = tostr.ip_tostr(ip_TGS)
    ts2 = time.time()
    ts2 = tostr.ts_tostr(ts2)

    lifetime2 = 666
    lifetime2 = tostr.lifetime_tostr(lifetime2)

    ip_Client = tostr.ip_tostr(ip_Client)

    ticket_tgs = get_ticket(Key_ctgs, ip_Client, ip_TGS, ts2, lifetime2, r)

    message = Key_ctgs + ip_TGS + ts2 + lifetime2 + ticket_tgs
    message = des_en.test(message, Key_c)
    return message

def AS():
    r = redis.Redis(host='localhost', port=6379, db=0)
    # 接受Client发送的报文
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    localhost = socket.gethostname()
    port = 10000
    s.bind((localhost,port))
    s.listen(5)

    cs,address = s.accept()
    print("got connection : ",address)

    try:
        message1 = cs.recv(1024)
    # message1 = '192.168.43.202*192.168.43.203*1556868720.719386*'
        receive = message1.decode()
        ip_Client = receive[0:15]
        ip_Client = tostr.takeout(ip_Client)
        print("ip_Client = ", ip_Client)  # 数据库判断是否合法的ip

        ip_TGS = receive[15:30]
        ip_TGS = tostr.takeout(ip_TGS)
        print("ip_TGS = ", ip_TGS)

        ts1 = receive[30:48]
        ts1 = tostr.takeout(ts1)
        print("ts1 = ", ts1)
        ip_c = (r.get('ip_Client')).decode()
        if ip_c == ip_Client:
            message2 = AS_to_Client(ip_Client, r)
            print("message2 = ", message2)
            # 发送message给Client
            cs.send(message2.encode())
        else:
            print("There is not ",ip_Client)
            s.close()
    except ConnectionResetError as e:
        print('关闭了正在占线的链接！')

    cs.close()


if __name__ == '__main__':
    AS()