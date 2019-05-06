import des_encryption as en
import des_decryption as de
import RSA as rsa
import AS as As
import TGS as Tgs
import Server as Server
import Client as Client
import time
import redis
import binascii


if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, db=0)
    print(r.get('Key_Client'))
    #As.AS()
    #Tgs.TGS()
    #Server.SERVER()
    #Client.CLIENT()


    #print("输入对称加密密钥：")
    #key1 = input()
    #print("输入要加密的明文：")
    #p = input()
    """time1 = time.time()

    key1 = '15489354'
    p = '1994年初秋，天气已经微凉，树叶的颜色早已老成暗淡，天空也老是阴沉沉的，空气中弥漫的令人窒息的静寂。家院子里的木瓜树直挺挺的立在那里，高挑而纤细，头部孤零零的挂着几个还未成熟的果实，也不知是个哪个捣蛋鬼竟拿石头丢的木瓜淌出了汁液，活像人的眼泪。母亲就是在这样的一个季节来到父亲家中的。当时家中有四兄弟父亲排行老四，一家人黑压压全部挤在这个用黄土堆砌成的小院子里，父亲的住处是用木板围成的不足20平米的小房间，母亲心里想着这么小的屋子放张床和衣柜人倒是就走不进去了，这陈旧的瓦房雨天估计还会漏雨。母亲心里本来就憋屈难受，哪知第二天大清早的，还未过门的三伯母娘家人听闻母亲的到来怒气冲冲的跑来告诫父亲，不允许父亲在三伯父之前成婚。母亲气坏了哪有人这么蛮横的，顺着这股气母亲干脆就走了。'
    ciphertext = en.test(p, key1)
    print("ciphertext = ", ciphertext)

    plaintext = de.test(ciphertext, key1)
    print("plaintext = ", plaintext)

    e,d,n = rsa.get_key()  # 非对称加密的密钥获取，或者自己设定也行

    ciphertext1 = rsa.encryption(p,e,n)
    print("rsa ciphertext = ", ciphertext1)
    plaintext1 = rsa.decryption(ciphertext1,d,n)
    print("rsa plaintext = ", plaintext1)

    time2 = time.time()
    print("time = ", 1000 * (time2 - time1), "ms")"""
