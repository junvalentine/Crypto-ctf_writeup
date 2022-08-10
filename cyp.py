from pwn import *
import sys
import math
import numpy
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes,getPrime, inverse
from Crypto.Util import number
from Crypto.Cipher import AES
from hashlib import sha256
from gmpy2 import *
import owiener
from random import getrandbits
from Crypto.Util.Padding import pad,unpad
import binascii
from egcd import egcd

conn = remote("04.cr.yp.toc.tf", 13777)
conn.sendlineafter(b"[Q]uit", b"G")
inp = conn.recvlinesS(4)
q = int(inp[1].split("= ")[1])
r = int(inp[2].split("= ")[1])
s = int(inp[3].split("= ")[1])
print(q,r,s)
conn.sendlineafter(b"[Q]uit", b"S")
ques = conn.recvlineS()
ques = conn.recvlineS()
l="| please send requested solution like x, y such that x is 14"
print(len(ques),ques,len(l))
i=0
while i<5 :
    k=int(ques[58:60])
    print(k)
    i += 1
    k=2**k-3
    if ques[53]=='y':
        ans = (r*inverse(s,q)*(k))%q
        conn.sendline(str(ans)+', '+str(k))
    else:
        ans = (s * inverse(r, q) * (k)) % q
        conn.sendline(str(k) + ', ' + str(ans))
    if i==5:
        out=conn.recvlineS()
    else:
        out=conn.recvlinesS(2)
    print(out)
    ques = out[1]

