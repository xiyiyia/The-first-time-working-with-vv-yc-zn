import binascii
import time
import math
import random

def __random_seed():
	seed = time.time()
	return math.sqrt(seed)
def __gcd(a, b):
    if b == 0:
        return a
    else:
        return __gcd(b, a % b)
def __random_inter():
	sum_n = 0
	key_part = []
	a = random.randint(1,5)

	for i in range(1,20):
		b = random.randint(1,5)
		c = random.random()
		while c < 0.1:
			c = random.random()
		key_part.append((int)(c*pow(10,b)))
		#key_part.append((int)(c*10))
	key = [str(x) for x in key_part]
	str_key = "".join(key)
	#print(str_key)
	return int(str_key)


def __ojmd_plus(a,b): #ax - by = gcd( a , b )
	if(b == 0):
		return a,b
	else:
		x2,y2 = __ojmd_plus(b, a%b)
		y1 = x2 - a // b * y2
		#print(y2,y1)
		return y2,y1
def __random_pq():
	pre_part = p = __random_inter()
	l = 0
	a = random.randint(0,79)
	while l < 6 :
		b = __random_inter()
		if(pow(b, p - 1, p) != 1):
			l = 0
			p = __random_inter()
			continue
		l += 1
	return p
def __en(M,e,n):
	result = 1
	after_mod = []
	pre_part = M
	after_mod.append(pre_part)
	bin_array = bin(e)[2:][::-1]
	for i in range(len(bin_array) -1):
			cur_part = (pre_part * pre_part)%n
			after_mod.append(cur_part)
			pre_part = cur_part
	for j in range(len(after_mod)):
		if not int(bin_array[j]):
			continue
		result *= after_mod[j]
		result = result%n
	return result
def __random_key():
	d = -1
	while d < 0:
		e = 3889
		five = 0
		while five <= e or __gcd(five, e) != 1:
			p = __random_pq()
			q = __random_pq()
			five = (p - 1)*(q - 1)
		#print(q,p)
		n = p*q
		d,l = __ojmd_plus(e,five)
		#print(d)
		#if d < 0:
			#print("false")

	return (e,n),(d,n)


def decompose(m):
	length = len(m)
	k = 1 + length // 10

	return k


def get_key():
	pub_key, pri_key = __random_key()
	e = pub_key[0]
	d = pri_key[0]
	if pub_key[1] != pri_key[1]:
		print("EORRO EORRO EORRO EORRO EORRO EORRO EORRO")
	else:
		n = pub_key[1]
	return e,d,n

def encryption(plaintext, e, n):

	M_str = plaintext
	ticks1 = time.perf_counter()
	k = decompose(M_str)
	C = ''
	length = len(M_str)
	#print("Length of M is: ", length)

	for i in range(0, k):
		if i == k-1:
			M_string = M_str[i*10:len(M_str)]
		else:
			M_string = M_str[i*10:(i+1)*10]
		ret = M_string.encode()
		#print(ret)
		ret1 = binascii.b2a_hex(ret)
		#print(ret1)
		ret2 = ret1.decode()
		#print("ret2 = ", ret2)
		M = int(ret2, 16)
		#print(M)
		if i == k-1:
			C += str(__en(M,e,n))
		else:
			C += (str(__en(M,e,n)) + '*')
	#print("C = ", C)
	ticks2 = time.perf_counter()
	#print(str((ticks2 - ticks1) * 1000) + "ms")
	return C


def decryption(C,d,n):
	P = ''
	st0 = C.split('*')
	#print("st0 = ", st0)
	#print("length of st0 = ", len(st0), st0[0])
	for i in range(len(st0)):
		#ret3 = hex(st0[i])
		#ret4 = ret3[2:]
		#print("ret4 = ", ret4)
		#print("C:",C)
		c = int(st0[i])
		#print(i, " = ", c)
		M = __en(c, d, n)
		#print("M:",M)
		ret5 = hex(M)
		#print("ret5 = ", ret5)
		ret6 = ret5[2:]
		ret7 = ret6.encode()
		ret8 = binascii.a2b_hex(ret7)
		#print("ret8 = ", ret8)
		ret9 = ret8.decode()
		#print("ret9 = ", ret9)
		P += ret9
	return P