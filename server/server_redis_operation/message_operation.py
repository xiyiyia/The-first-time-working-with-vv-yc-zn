#! /usr/bin/python


import server.server_redis_operation.json_operation as json_operation
import server.server_redis_operation.data_operation.intergrated_message as intergrated_message
import server.data_operation.message_pb2 as message_pb2
import operator as op
import server.server_redis_operation.redis_operation as redis_operation
import server.server_redis_operation.server_message_creat as server_message_creat
import logging


class MessageOperation:
    @staticmethod
    def server_operation(mes_3):
        logging.basicConfig(level=logging.DEBUG)
        LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
        logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)
        LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
        DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

        # message = recv()
        # message = type1 + message1
        redis_1 = redis_operation.RedisOperation()
        im_1 = message_pb2
        smc_1 = server_message_creat.ServerMessageCreator()
        json_1 = json_operation.JsonServer()

        mes = im_1.GeneralMessages()
        mes_1 = mes_3
        mes.ParseFromString(mes_3[2:])
        if op.eq(mes_1[0:1], '00'):
            mes = im_1.GeneralMessages()
            mes_send = im_1.GeneralMessages()
            # mes_data = im_1.signup()
            mes_send_DID = im_1.GeneralMessages()

            mes.ParseFromString(message1)
            if op.eq(mes.RC, '000001'):
                # signup
                logging.info(mes)
                mes_data = im_1.gm_signup()
                mes_data.ParseFromString(mes.DATA)
                if redis_1.check_id_exists(mes_data.ID):
                    if redis_1.check_signup(mes_data.ID, mes_data.PSW):
                        mes_send = smc_1.signup(mes, 1)
                        redis_1.std_signup(mes_data.ID, mes_data.PSW)
                        logging.info(mes_send)
                        json_1.update_json(mes_data.ID)
                        # send(mes_send, mes.SIP)
                        # send json
                    else:
                        mes_send = smc_1.signup(mes, 2)
                        logging.info(mes_send)
                        # send(mes_send, mes.SIP)
                else:
                    mes_send = smc_1.signup(mes, 3)
                    logging.info(mes_send)
            if op.eq(mes.RC, '001001'):
                # signin
                logging.info(mes)
                mes_data = im_1.gm_signup()
                mes_data.ParseFromString(mes.DATA)
                if not redis_1.check_id_exists(mes_data.ID):
                    redis_1.user_login(mes_data.ID, mes_data.PSW)
                    mes_send = smc_1.signup(mes, 1)
                    logging.info(mes_send)
                    # send(mes_send, mes.SIP)
                    # send json
                else:
                    mes_send = smc_1.login(mes, 2)
                    logging.info(mes_send)
            if op.eq(mes.RC, '000010'):
                # add friend
                logging.info(mes)
                mes_data = im_1.gm_friend()
                mes_data.ParseFromString(mes.DATA)
                if op.eq(mes.SC, '66666'):
                    mes_send_SID = smc_1.add_friend(mes, mes_data, 2)
                    json_1.add_friend_json(mes_data.SID, mes_data.DID)
                    json_1.update_json(mes_data.SID)
                    json_1.update_json(mes_data.DID)
                    # send(mes_send_SID)
                    # send double json to SID,DID
                if op.eq(mes.SC, '00010'):
                    mes_send_SID = smc_1.add_friend(mes, mes_data, 4)
                    # send(mes_send_SID)

                if redis_1.check_id_exists(mes_data.DID):
                    mes_send_DID = smc_1.add_friend(mes, mes_data, 1)
                    # send(mes_send_DID)

                else:
                    mes_send = smc_1.add_friend(mes, mes_data, 3)
                    logging.info(mes_send)
                    # send(mes_send)
            if op.eq(mes.RC, '000011'):
                # delete friend
                logging.info(mes)
                mes_data = im_1.GeneralMessages()
                mes_data.ParseFromString(mes.DATA)

                if redis_1.check_id_exists(mes_data.DID):
                    mes_send = smc_1.delete_friend(mes, 1)
                    json_1.add_friend_json(mes_data.SID, mes_data.DID)
                    json_1.update_json(mes_data.SID)
                    json_1.update_json(mes_data.DID)
                    # send(mes_send)
                    # send double json to SID,DID
                else:
                    mes_send = smc_1.add_friend(mes, mes_data, 2)
                    logging.info(mes_send)
                    # send(mes_send)
            '''
            if op.eq(mes.RC, '010001'):
            if op.eq(mes.RC, '010001'):
            if op.eq(mes.RC, '010001'):
            if op.eq(mes.RC, '010001'):
            '''
        '''
        if op.eq(type, '01'):
            mes = im_1.ClientAS()
        if op.eq(type, '02'):
            mes = im_1.AuthenticatorC3()
        if op.eq(type, '03'):
            mes = im_1.ClientV()
        if op.eq(type, '04'):
            mes = im_1.AuthenticatorC5()
        if op.eq(type, '05'):
            mes = im_1.VClient()
        if op.eq(type, '06'):
            mes = im_1.ClientTGS()
        if op.eq(type, '07'):
            mes = im_1.TGSClient()
        if op.eq(type, '08'):
            mes = im_1.Ticketv()
        if op.eq(type, '09'):
            mes = im_1.ASClient()
        if op.eq(type, '10'):
            mes = im_1.Tickettgs()
        '''