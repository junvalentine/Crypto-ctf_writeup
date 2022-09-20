# nhận thấy rằng các function chỉ để che mắt, các công thức của key và enc mới là qtrong.
# flag = key ^ aniely_stream(key) ^ enc ^ rand (rand tự gen) 
from Crypto.Util.number import *
from gmpy2 import *
from pwn import *
from struct import *

key = "4dcceb8802ae3c45fe80ccb364c8de19f2d39aa8ebbfb0621623e67aba8ed5bc"
enc = "e67a67efee3a80b66af0c33260f96b38e4142cd5d9426f6f156839f2e2a8efe8"
enc=bytes.fromhex(enc)
key=bytes.fromhex(key)
for i in range(255):
    for j in range(255):
        rand=(long_to_bytes(i)+long_to_bytes(j)) *16
        #print(rand)
        anie=aniely_stream(key)
        ans=bytes(a^b^c^d for a,b,c,d in zip(key,anie,enc,rand))
        if ans[:2]==b"CC":
            print(ans)
      
#b'CCTF{7rY_t0_D3cRyPT_z3_ChaCha20}'      
