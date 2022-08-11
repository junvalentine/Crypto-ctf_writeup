from pwn import *
from base64 import *

#Xor with known text thêm base64
f=open("C:/Users/lehon/Downloads/baphomet_fdf9601f7b73b004bee77ccb6e30913c544ef2a1 (1)/baphomet/flag.enc","rb")
a=f.read()
x=b"q0nurN" 
#Q0NURn trong base64 là CCTF

y=a[:6]
#y là ct lấy 6 kí tự đầu

key=b''
for i in range(len(y)):
	key += (x[i] ^ y[i % len(y)]).to_bytes(1, 'big')

x1 =a
enc = b''
for i in range(len(x1)):
	enc += (x1[i] ^ key[i % len(key)]).to_bytes(1, 'big')

encc="q0nurNTvCfaZCL8WuL9St3DfuL8Xn1PFDeGZx1bYmgjmm019"
#enc type string :D
ans=''
for b in encc:
	if b.islower():
		ans += b.upper()
	else:
		ans += b.lower()
print(b64decode(ans))

#b'CCTF{UpP3r_0R_lOwER_17Z_tH3_Pr0bL3M}'


