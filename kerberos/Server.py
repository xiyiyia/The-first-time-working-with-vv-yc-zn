import kerberos.des_decryption as des_de
import kerberos.des_encryption as des_en
import kerberos.Tstr as tostr
import socket


def Server_to_Client(ts5, Key_cv):
    ts5 += 1
    ts5 = tostr.ts_tostr(ts5)
    message = des_en.test(ts5, Key_cv)
    return message


def SERVER():
    Key_server = 'bcdefgh'
    #message5 = '928F4FE9A2F3D3CED3D397336CC8B2EEEC307CAEB9A0471F8127A8CFD08E295189D108A74C4DD9D61666640358B672B00FBB826366B28F2BBC712109B4856D6EA4910B74D4E183C668ED77CEC893F50B9B2431C2F876C9CA2DDB21338EE8003F4421A988FA40BBB991D4E08E7FA7594CF47D82B5A28666B16460CABC8840EF21E9AB683C1432B9B0'
    #lenofticket_server = '160'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    localhost = socket.gethostname()
    port = 10002
    s.bind(("localhost", port))
    s.listen(5)

    cs, address = s.accept()
    print("got connection : ", address)

    message5 = cs.recv(1024)
    message5 = message5.decode()
    print("messge5 = ", message5)
    lenofticket = cs.recv(1024)
    lenofticket_server = lenofticket.decode()
    print("len = ", lenofticket)

    ticket_server = message5[0:int(lenofticket_server)]
    ticket_server = des_de.test(ticket_server,Key_server)
    ticket_server = tostr.takeout(ticket_server)
    print("ticket_server = ", ticket_server)

    Key_cv = ticket_server[0:7]
    print("Key_cv = ", Key_cv)
    ip_Client = ticket_server[7:22]
    ip_Client = tostr.takeout(ip_Client)
    print("ip_Client = ", ip_Client)

    AD_client = ticket_server[22:37]
    AD_client = tostr.takeout(AD_client)
    print("AD_client = ", AD_client)

    ip_Server = ticket_server[37:52]
    ip_Server = tostr.takeout(ip_Server)
    print("ip_Server = ", ip_Server)

    ts4 = ticket_server[52:70]
    ts4 = tostr.takeout(ts4)
    print("ts4 = ", ts4)

    lifetime4 = ticket_server[70:78]
    lifetime4 = tostr.takeout_0(lifetime4)
    print("lifetime4 = ", lifetime4)

    Authencator_c = message5[int(lenofticket_server):len(message5)]
    Authencator_c = des_de.test(Authencator_c,Key_cv)
    print("Authencator_c = ",Authencator_c)

    ip_Client_fromAu = Authencator_c[0:15]
    ip_Client_fromAu = tostr.takeout(ip_Client_fromAu)
    print("ip_Client_fromAu = ", ip_Client_fromAu)

    AD_client_fromAu = Authencator_c[15:30]
    AD_client_fromAu = tostr.takeout(AD_client_fromAu)
    print("AD_client_fromAu = ", AD_client_fromAu)

    ts5 = Authencator_c[30:]
    ts5 = tostr.takeout(ts5)
    ts5 = float(ts5)
    print("ts5 = ",ts5)

    message6 = Server_to_Client(ts5,Key_cv)
    print("message6 = ", message6)

    cs.send(message6.encode())
    cs.close()


if __name__ == '__main__':
    SERVER()