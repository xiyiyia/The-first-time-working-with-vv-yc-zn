#! /usr/bin/python
import server.server_redis_operation.data_operation.intergrated_message as intergrated_message
import server.server_redis_operation.data_operation.message_pb2 as message_pb2

class ServerMessageCreator:
    @staticmethod
    def signup(mes_1, type_1):
        im = message_pb2
        mes_2 = im.GeneralMessages()
        if type_1 == 1:
            mes_2.SIP = mes_1.DIP
            mes_2.DIP = mes_1.SIP
            mes_2.DATA = '0'
            mes_2.RC = '010001'
            mes_2.SC = '66666'
            mes_2.DT = '00'
            return mes_2
        if type_1 == 2:
            mes_2.SIP = mes_1.DIP
            mes_2.DIP = mes_1.SIP
            mes_2.DATA = '0'
            mes_2.RC = '010001'
            mes_2.SC = '00001'
            mes_2.DT = '00'
            return mes_2
        if type_1 == 3:
            mes_2.SIP = mes_1.DIP
            mes_2.DIP = mes_1.SIP
            mes_2.DATA = '0'
            mes_2.RC = '010001'
            mes_2.SC = '00100'
            mes_2.DT = '00'
            return mes_2

    @staticmethod
    def login(mes_1, type_1):
        im = message_pb2
        mes_2 = im.GeneralMessages()
        if type_1 == 1:
            mes_2.SIP = mes_1.DIP
            mes_2.DIP = mes_1.SIP
            mes_2.DATA = '0'
            mes_2.RC = '011001'
            mes_2.SC = '66666'
            mes_2.DT = '00'
            return mes_2
        if type_1 == 2:
            mes_2.SIP = mes_1.DIP
            mes_2.DIP = mes_1.SIP
            mes_2.DATA = '0'
            mes_2.RC = '011001'
            mes_2.SC = '00011'
            mes_2.DT = '00'
            return mes_2

    @staticmethod
    def add_friend(mes_1, mes_data2, type_1):
        im = message_pb2
        mes_2 = im.GeneralMessages()
        if type_1 == 1:
            mes_2.SIP = mes_1.DIP
            mes_2.DIP = mes_data2.DIP
            mes_2.DATA = mes_1.DATA
            mes_2.RC = '010010'
            mes_2.SC = '00000'
            mes_2.DT = '00'
            return mes_2
        if type_1 == 2:
            mes_2.SIP = mes_1.DIP
            mes_2.DIP = mes_data2.SIP
            mes_2.DATA = mes_1.DATA
            mes_2.RC = '010010'
            mes_2.SC = '66666'
            mes_2.DT = '00'
            return mes_2
        if type_1 == 3:
            mes_2.SIP = mes_1.DIP
            mes_2.DIP = mes_1.SIP
            mes_2.DATA = '0'
            mes_2.RC = '010010'
            mes_2.SC = '00100'
            mes_2.DT = '00'
            return mes_2
        if type_1 == 4:
            mes_2.SIP = mes_1.DIP
            mes_2.DIP = mes_data2.SIP
            mes_2.DATA = '0'
            mes_2.RC = '010010'
            mes_2.SC = '00010'
            mes_2.DT = '00'
            return mes_2

    @staticmethod
    def delete_friend(mes_1, type_1):
        im = message_pb2
        mes_2 = im.GeneralMessages()
        if type_1 == 1:
            mes_2.SIP = mes_1.DIP
            mes_2.DIP = mes_1.SIP
            mes_2.DATA = '0'
            mes_2.RC = '010011'
            mes_2.SC = '66666'
            mes_2.DT = '00'
            return mes_2
        if type_1 == 2:
            mes_2.SIP = mes_1.DIP
            mes_2.DIP = mes_1.SIP
            mes_2.DATA = '0'
            mes_2.RC = '010011'
            mes_2.SC = '00100'
            mes_2.DT = '00'
            return mes_2