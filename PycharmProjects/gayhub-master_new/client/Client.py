import des_decryption as des_de
import des_encryption as des_en
import Tstr as tostr
import socket
import time


def Client_to_AS():
    ip_Client = tostr.get_host_ip()
    ip_Client = tostr.ip_tostr(ip_Client)
    print("ip = ", ip_Client)

    ip_TGS = "192.168.43.203"
    ip_TGS = tostr.ip_tostr(ip_TGS)
    print("ip_TGS = ", ip_TGS)

    ts1 = time.time()
    ts1 = tostr.ts_tostr(ts1)
    print("ts1 = ", ts1)

    #str_ClienttoAS = tostr.IntegrationMessage.ClientAS(ip_Client, ip_TGS, ts1)
    str_ClienttoAS = ip_Client + ip_TGS + ts1
    print("str_Client = ", str_ClienttoAS)

    return str_ClienttoAS


def get_Authencator(Key_ctgs):
    ip_Client = tostr.get_host_ip()
    ip_Client = tostr.ip_tostr(ip_Client)

    AD_c = ip_Client

    ts3 = time.time()
    ts3 = tostr.ts_tostr(ts3)

    authencator = ip_Client + AD_c + ts3
    authencator = des_en.test(authencator, Key_ctgs)

    return authencator,ts3


def Client_to_TGS(ticket_TGS, Key_ctgs):
    ip_Server = '192.168.43.204'  # 如何获取SERVER端的IP呢************************************************

    ip_Server = tostr.ip_tostr(ip_Server)

    Authenticator_c,ts = get_Authencator(Key_ctgs)

    message = ip_Server + ticket_TGS + Authenticator_c
    return message,str(len(ticket_TGS))


def Client_to_Server(ticket_Server, Key_cv):
    Authencator_c,ts5 = get_Authencator(Key_cv)

    message = ticket_Server + Authencator_c
    return message, len(ticket_Server),ts5


def CLIENT():
    Key_c = 'abcdefg'  # Key_Client
    message1 = Client_to_AS()
    localhost = socket.gethostname()
    port_AS = 10000
    port_TGS = 10001
    port_Server = 10002
    print("mesage1 = ", message1)

    """s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((localhost,port_AS))
    s.send(message1.encode('utf-8'))
    message2 = s.recv(1024)
    message2 = message2.decode()
    print("message2 = ",message2)
    s.close()"""

    message2 = 'D3A41D74DCE667CA3EC5834761094B6107687B4A2EAAD82C7D6C097A8D60C4B35DF32FDC8FF799DE98B3A781D438F4A6D937FF4846783646DCB15C599E2C137B9D16D5F49BB06BDEB47FD74D78ED5812E0B93D9376E96BF7274E7E3D56629190EA06D02563EC5238CB237E0D07B3FBE21F2B042DAE997E4CF0A64B564FBB3B0D72912ACA208A52D0186ED178DC91FC91A411BF971D3D6122E8B5DEDAD7E7459C06C31C384C2E3E3CA0F0BBADF3CBF4010D5473F8A9F64FD5C684031231C9999BAD0E6439F7333D2E47AAA1EB7B5E0CDCE9AB683C1432B9B0'
    message2 = des_de.test(message2, Key_c)
    print("message2 = ", message2)
    Key_ctgs = message2[0:7]
    print("Key_ctgs = ", Key_ctgs)

    ip_TGS_fromAS = message2[7:22]
    ip_TGS_fromAS = tostr.takeout(ip_TGS_fromAS)
    print("ip_TGS = ", ip_TGS_fromAS)

    ts2 = message2[22:40]
    ts2 = tostr.takeout(ts2)
    ts2 = float(ts2)
    print("ts2 = ", ts2)

    lifetime2 = message2[40:48]
    lifetime2 = tostr.takeout_0(lifetime2)
    print("lifetime2 = ", lifetime2)

    ticket_TGS = message2[48:]
    print("ticket_TGS = ", ticket_TGS)
    # 给TGS发送报文

    message3,lenofticket_tgs = Client_to_TGS(ticket_TGS,Key_ctgs)
    print("message3 = ", message3)
    print("lenofticket = ", lenofticket_tgs)
    # 发送报文到TGS，再把lenofticket也发送过去
    """tgs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("1")
    tgs.connect(("localhost", port_TGS))
    print("2")

    tgs.send(message3.encode('utf-8'))
    print("3")
    time.sleep(1)
    tgs.send(lenofticket_tgs.encode('utf-8'))
    message4 = tgs.recv(1024)
    message4 = message4.decode()
    print("message4 = ", message4)
    tgs.close()"""
    # 从TGS接收到message4
    message4 = '7ECB2D091E65A2B0D76FA69341FB845BEA16784472B24B61A4937E2B6F781BB20A7BB2D208888E679F9BC69CE2078306AE7A9BC210F3BE425BF00DC80C8355CFCCD728A6DF641CB97AF7F85421A0B79F3258DC5EEF1F640B3DF01E1B3537772D33F85F8265EF443CD1028570A2B639F434B4EFDECC61F27B65197A570A5E4DA5F7242F37BD68F4A81F69A771D36883CF0E533063C1E9428D9FB361FC1450E8717C5CBE5AF3B877E6BBFB26A32C116E1FBD161581C15540BACC130C743E83F60867D77BE9F9CC2B0E7358F0ED7796932F'
    message4 = des_de.test(message4, Key_ctgs)
    message4 = tostr.takeout(message4)
    print("message4 = ", message4)
    lenofmessage4 = len(message4)
    Key_cv = message4[0:7]
    print("Key_cv = ", Key_cv)

    ip_Server = message4[7:22]
    ip_Server = tostr.takeout(ip_Server)
    print("ip_Server = ", ip_Server)

    ts4 = message4[22:40]
    ts4 = tostr.takeout(ts4)
    print("ts4 = ", ts4)

    ticket_Server = message4[40:lenofmessage4]

    print("ticket_Server = ", ticket_Server)

    message5, lenofticket_server, ts5 = Client_to_Server(ticket_Server, Key_cv)
    lenofticket_server = str(lenofticket_server)
    print("message5 = ", message5)
    print("lenofticket_server = ", lenofticket_server)
    print("ts5 = ", ts5)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(("localhost", port_Server))
    server.send(message5.encode('utf-8'))
    time.sleep(1)
    server.send(lenofticket_server.encode('utf-8'))
    message6 = server.recv(1024)
    message6 = message6.decode()
    print("message6 = ", message6)
    server.close()
    message6 = des_de.test(message6, Key_cv)
    ts6 = tostr.takeout(message6)
    print("ts6 = ", ts6)


if __name__ == '__main__':
    CLIENT()