from pwn import *
from Crypto.Util.number import inverse

conn = remote("04.cr.yp.toc.tf", 13777)
conn.sendlineafter(b"[Q]uit", b"G")
inp = conn.recvlinesS(4)
q = int(inp[1].split("= ")[1])
r = int(inp[2].split("= ")[1])
s = int(inp[3].split("= ")[1])

conn.sendlineafter(b"[Q]uit", b"S")
ques = conn.recvlineS()
ques = conn.recvlineS()

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
  
#Congrats, you got the flag: CCTF{f1nDin9_In7Eg3R_50Lut1Ons_iZ_in73rEStIn9!}
