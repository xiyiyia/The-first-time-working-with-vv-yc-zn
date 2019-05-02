#! /usr/bin/python

import data_operation.message_pb2 as message_pb2
import operator as op


class MessageOperation:
    @staticmethod
    def get_message(mes):
        mes_1 = mes
        mes_2 = message_pb2.GeneralMessages()
        mes_2.ParseFromString(mes[2:])
        if op.eq(mes_1[0:1], '00'):
            return mes_2.RC, mes_2.SC, mes_2.DATA, mes_2.SIP, mes_2.DIP
