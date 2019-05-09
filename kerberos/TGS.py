import kerberos.des_encryption as des_en
import kerberos.des_decryption as des_de
import kerberos.Tstr as tostr
import time
import socket
import random


def get_ticket(ip_Client,AD_Client,ip_Server,Key_cv,Key_server):
    ts4 = time.time()
    ts4 = tostr.ts_tostr(ts4)

    lifetime4 = 666
    lifetime4 = tostr.lifetime_tostr(lifetime4)

    ticket_Server = Key_cv + ip_Client + AD_Client + ip_Server + ts4 + lifetime4
    ticket_Server = des_en.test(ticket_Server, Key_server)
    print("ticket_server = ", ticket_Server)
    return ticket_Server,ts4


def get_key():
    list_key = ['afghijk','bfghijk','cfghijk','dfghijk','efghijk','ffghijk','gfghijk','hfghijk','ifghijk','jfghijk','kfghijk','lfghijk','mfghijk','nfghijk','ofghijk','pfghijk','qfghijk','rfghijk','sfghijk','tfghijk','ufghijk','vfghijk','wfghijk','xfghijk','yfghijk','zfghijk']
    key = random.choice(list_key)
    return key

def TGS_to_Client(ip_Client, ip_Server, Key_ctgs):

    Key_server = 'bcdefgh'
    Key_server = tostr.ip_tostr(Key_server)
    Key_cv = get_key()
    Key_server = tostr.ip_tostr(Key_server)

    ip_Server = tostr.ip_tostr(ip_Server)
    ip_Client = tostr.ip_tostr(ip_Client)
    AD_Client = ip_Client
    ticket_Server,ts4 = get_ticket(ip_Client,AD_Client,ip_Server,Key_cv,Key_server)
    message = Key_cv + ip_Server + ts4 + ticket_Server
    message = des_en.test(message, Key_ctgs)
    print("message = ", message)
    return message


def TGS():
    Key_tgs = 'cdefghi'
    # 从Client接收message3
    # 从Client接收lenofticket(str型)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    localhost = socket.gethostname()
    port = 10001
    s.bind(("localhost", port))
    s.listen(5)

    cs, address = s.accept()
    print("got connection : ", address)

    message3 = cs.recv(1024)
    message3 = message3.decode()
    print("messge3 = ", message3)
    print("1")
    lenofticket = cs.recv(1024)
    print("2")
    lenofticket = lenofticket.decode()
    print("len = ", lenofticket)


    #message3 = '192.168.43.204*928F4FE9A2F3D3CED3D397336CC8B2EEEC307CAEB9A0471F8127A8CFD08E295189D108A74C4DD9D61666640358B672B03E3CE0B836AE132C175F44F4F1488D50072D6EE80E2A596368ED77CEC893F50B********6662F19DEF926DBD87A95C21E5C4C0D3D3D397336CC8B2EEFF08097D8012F6E2A02087B20DB77FE24536257798F303C3E9AB683C1432B9B0'
    lenofmessage = len(message3)
    # lenofticket = '168'
    ip_Server = message3[0:15]
    ip_Server = tostr.takeout(ip_Server)

    ticket_TGS = message3[15:int(lenofticket) + 15]
    ticket_TGS = tostr.takeout(ticket_TGS)
    ticket_TGS = des_de.test(ticket_TGS, Key_tgs)
    print("ticket_TGS = ", ticket_TGS)

    Key_ctgs_fromclient = ticket_TGS[0:7]
    ip_Client_fromclient = ticket_TGS[7:22]
    ip_Client_fromclient = tostr.takeout(ip_Client_fromclient)
    print("ip_Client_fromclient = ", ip_Client_fromclient)

    AD_Client_fromclient = ticket_TGS[22:37]
    AD_Client_fromclient = tostr.takeout(AD_Client_fromclient)
    print("AD_Client_fromclient = ", AD_Client_fromclient)

    ip_TGS_fromclient = ticket_TGS[37:52]
    ip_TGS_fromclient = tostr.takeout(ip_TGS_fromclient)
    print("ip_TGS_fromclient = ", ip_TGS_fromclient)

    ts2_fromclient = ticket_TGS[52:70]
    ts2_fromclient = tostr.takeout(ts2_fromclient)
    print("ts2_fromclient = ", ts2_fromclient)

    lifetime2_fromclient = ticket_TGS[70:78]
    lifetime2_fromclient = tostr.takeout_0(lifetime2_fromclient)
    print("lifetime2 = ", lifetime2_fromclient)

    Authencator_client = message3[int(lenofticket) + 15:lenofmessage]
    Authencator_client = tostr.takeout(Authencator_client)
    Authencator_client = des_de.test(Authencator_client, Key_ctgs_fromclient)
    print("Authencator_c = ", Authencator_client)

    ip_Client_fromclient2 = Authencator_client[0:15]
    ip_Client_fromclient2 = tostr.takeout(ip_Client_fromclient2)
    print("ip_Client_fromclient2 = ", ip_Client_fromclient2)

    AD_Client_fromclient2 = Authencator_client[15:30]
    AD_Client_fromclient2 = tostr.takeout(AD_Client_fromclient2)
    print("AD_Client_fromclient2 = ", AD_Client_fromclient2)

    ts3_fromclient = Authencator_client[30:48]
    ts3_fromclient = tostr.takeout(ts3_fromclient)
    print("ts3 = ", ts3_fromclient)

    message4 = TGS_to_Client(ip_Client_fromclient, ip_Server, Key_ctgs_fromclient)
    print("message4 = ", message4)

    cs.send(message4.encode())

    cs.close()


if __name__ == "__main__":
    TGS()