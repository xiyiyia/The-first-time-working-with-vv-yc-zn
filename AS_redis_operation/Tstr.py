import socket


def key_tostr(key):
    key = str(key)
    if len(key) < 7:
        l = 7 - len(key)
        for i in range(0, l):
            key += '*'
    elif len(key) > 7:
        key = key[0:7]
    return key


def lifetime_tostr(lifetime):
    lifetime = str(lifetime)
    length = len(lifetime)
    if length > 8:
        lifetime = lifetime[0:8]
    else:
        for i in range(0, 8-length):
            lifetime = '0' + lifetime
    return lifetime


def takeout(a):
    length = len(a)
    while a[length-1] == '*':
        a = a[0:length-1]
        length = len(a)
    return a


def takeout_0(lifetime):
    length = len(lifetime)
    while lifetime[0] == '0':
        lifetime = lifetime[1:length]
        length = len(lifetime)
    lifetime = int(lifetime)
    return lifetime


def ts_tostr(ts):
    ts = str(ts)
    length = len(ts)
    for i in range(0, 18-length):
        ts += '*'
    return ts


def ip_tostr(ip):
    ip_str = str(ip)
    length = len(ip_str)
    for i in range(0, 15-length):
        ip_str += '*'
    return ip_str


def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


