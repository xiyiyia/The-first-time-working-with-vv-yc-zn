import data_operation.message_pb2 as message_pb2


class IntegrationMessage:

    @staticmethod
    def gm_signup(id1, psw1):
        mes = message_pb2.gm_signup()
        mes.ID = id1
        mes.PSW = psw1
        return bytes.decode(mes.SerializeToString())

    @staticmethod
    def gm_friend(sid1, did1):
        mes = message_pb2.gm_friend()
        mes.SID = sid1
        mes.DID = did1
        return bytes.decode(mes.SerializeToString())

    @staticmethod
    def general_messages(rc1, sc1, dt1, data1, sip1, dip1):
        mes = message_pb2.GeneralMessages()
        mes.RC = rc1
        mes.SC = sc1
        mes.DT = dt1
        mes.DATA = data1
        mes.SIP = sip1
        mes.DIP = dip1
        return bytes.decode(mes.SerializeToString())

    @staticmethod
    def ClientAS(idc1, idtgs, ts1):
        mes = message_pb2.ASClient()
        mes.Kctgs = idc1
        mes.IDtgs = idtgs
        mes.TS1 = ts1
        return bytes.decode(mes.SerializeToString())

    @staticmethod
    def AuthenticatorC3(idc1, adc1, ts3):
        mes = message_pb2.ASClient()
        mes.IDc = idc1
        mes.ADc = adc1
        mes.TS3 = ts3
        return bytes.decode(mes.SerializeToString())

    @staticmethod
    def ClientV(ticketv1, authenticatorc):
        mes = message_pb2.ASClient()
        mes.Ticketv = ticketv1
        mes.AuthenticatorC = authenticatorc
        return bytes.decode(mes.SerializeToString())

    @staticmethod
    def AuthenticatorC5(idc1, adc1, ts5):
        mes = message_pb2.ASClient()
        mes.IDc = idc1
        mes.ADc = adc1
        mes.TS5 = ts5
        return bytes.decode(mes.SerializeToString())

    @staticmethod
    def VClient(ts5):
        mes = message_pb2.ASClient()
        mes.TS5 = ts5
        return bytes.decode(mes.SerializeToString())

    @staticmethod
    def ClientTGS(idv1, tickettgs1, authenticatorc1):
        mes = message_pb2.ASClient()
        mes.IDv = idv1
        mes.Tickettgs = tickettgs1
        mes.AuthenticatorC = authenticatorc1
        return bytes.decode(mes.SerializeToString())

    @staticmethod
    def TGSClient(kcv1, idv1, ts4, ticketv1):
        mes = message_pb2.ASClient()
        mes.Kcv = kcv1
        mes.IDv = idv1
        mes.TS4 = ts4
        mes.Ticketv = ticketv1
        return bytes.decode(mes.SerializeToString())

    @staticmethod
    def Ticketv(kcv1, idc1, adc1, idv1, ts4, lifetime4):
        mes = message_pb2.ASClient()
        mes.Kcv = kcv1
        mes.IDc = idc1
        mes.ADc = adc1
        mes.IDv = idv1
        mes.TS4 = ts4
        mes.Lifetime4 = lifetime4
        return mes.SerializeToString

    @staticmethod
    def ASClient(kctgs1, idtgs, ts2, lifetime2, tickettgs):
        mes = message_pb2.ASClient()
        mes.Kctgs = kctgs1
        mes.IDtgs = idtgs
        mes.TS2 = ts2
        mes.Lifetime2 = lifetime2
        mes.Tickettgs = tickettgs
        return bytes.decode(mes.SerializeToString())

    @staticmethod
    def Tickettgs(kctgs1, idc, adc, idtgs, ts2, lifetime2):
        mes = message_pb2.ASClient()
        mes.Kctgs = kctgs1
        mes.IDc = idc
        mes.ADc = adc
        mes.IDtgs = idtgs
        mes.TS2 = ts2
        mes.Lifetime2 = lifetime2
        return bytes.decode(mes.SerializeToString())