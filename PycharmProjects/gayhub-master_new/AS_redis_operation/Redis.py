import redis


def to_get(a):
    r = redis.Redis(host='localhost', port=6379, db=0)
    get_str = r.get(a).decode()
    print("get_str = ", get_str)
    return get_str


def do_redis():
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set('Key_Client','abcdefg')  # AS和Client之间的会话对称密钥
    r.set('Key_Server','bcdefgh')  # TGS和Server之间的会话对称密钥，应该存在TGS那里
    r.set('Key_TGS','cdefghi')  # AS和TGS之间的会话对称密钥
    r.set('Key_ctgs', 'defghij')
    r.set('Key_cv', 'efghijk')
    r.set('ip_Client','172.29.229.178')  # Client的标识，采用ip地址来表示
    r.set('ip_TGS','172.29.229.179')  # TGS的标识，采用ip地址来表示
    r.set('ip_Server','172.29.229.180')  # Server的标识，采用ip地址来表示

    r.save()
    print(to_get('Key_Client'))
    #print(r.client_list())  # 可以看出两个连接的id是一致的，说明是一个客户端连接

if __name__ == '__main__':
    do_redis()
    """
    1、在客户端怎么得到TGS和SERVER端的IP地址
    2、TGS这边要存有client--server的会话密钥，存在哪里？数据库吗还是直接存在代码里？
    3、大致还有的问题就是一个是UI设计，一个是各个部分怎么去验证，然后才打算回消息，我在这里是直接给回了
    """
    """
    1、加密解密的调用，在main函数里有示例
    2、DES加密解密是来嗯个文件、RSA是一个文件，两个不同的函数
    """