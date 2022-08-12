from pwn import *

# Bài này tuy đơn giản nhưng lại ít người làm :D. Đề cho 1 pt Diophantine 1337(z^4 - x^2) = 31337(y^2 - z^4) 
# và yêu cầu tìm nghiệm (x,y,z) với z có độ dài từ 30 đến 48 bit. Ta tìm được một bộ nghiệm là x=y=z^2.

conn=remote("02.cr.yp.toc.tf",17113)
step=30
for i in range(19):
    x=pow(2**(step+i)-1,2)
    z=2**(step+i)-1
    conn.sendlineafter(b"bit:",str(x)+", "+str(x)+", "+str(z))
ans=conn.recvlinesS(2)
print(ans)

#[' ', '| Congrats, you got the flag: CCTF{4_diOpH4nT1nE_3Qua7i0n__8Y__Jekuthiel_Ginsbur!!}']




