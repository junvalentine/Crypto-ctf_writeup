#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|  Hey math experts, in this challenge we will deal with the numbers   |
#|  those are the sum of two perfect square, now try hard to find them! |##
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||##|
#| Generating the `n', please wait..##.
#| Options##:
#|       [G##]et the n
#|       [S#]#olve the challenge!
#|       [Q#]u#it
#G
#| n = 1700915129667195972895306747621172339223172447368434887800097916055770689
#| Options:
#|       [G]et the n
#|       [S]olve the challenge!
#|       [Q]uit
#S
#| Send your pair x, y here:
#1241392430817362741242892791067588385, 399824914652095227757674083460181408
#| Congratz! the flag is CCTF{3Xpr3sS_4z_Th3_sUm_oF_7w0_Squ4rE5!}

#Source :https://math.stackexchange.com/questions/5877/efficiently-finding-two-squares-which-sum-to-a-prime
#Search gg thì ta thấy một thuật toán giúp tìm 2 số có tổng bp bằng 1 snt. Từ n ta ptich thành 3 số nguyên tố , 
# kết hợp áp dụng công thức (a^2+b^2)(c^2+d^2)=(ac+bd)^2+(ad-bc)^2   2 lần. Vấn đề duy nhất ở đây là việc factorize n qua tool có vẻ hơi thiếu tự nhiên :D 
# hoặc đề cố tình cho n nhỏ cho ta factor :)).

def mods(a, n):
    if n <= 0:
        return "negative modulus"
    a = a % n
    if (2 * a > n):
        a -= n
    return a

def powmods(a, r, n):
    out = 1
    while r > 0:
        if (r % 2) == 1:
            r -= 1
            out = mods(out * a, n)
        r //= 2
        a = mods(a * a, n)
    return out

def quos(a, n):
    if n <= 0:
        return "negative modulus"
    return (a - mods(a, n))//n

def grem(w, z):
    # remainder in Gaussian integers when dividing w by z
    (w0, w1) = w
    (z0, z1) = z
    n = z0 * z0 + z1 * z1
    if n == 0:
        return "division by zero"
    u0 = quos(w0 * z0 + w1 * z1, n)
    u1 = quos(w1 * z0 - w0 * z1, n)
    return(w0 - z0 * u0 + z1 * u1,
           w1 - z0 * u1 - z1 * u0)

def ggcd(w, z):
    while z != (0,0):
        w, z = z, grem(w, z)
    return w

def root4(p):
    # 4th root of 1 modulo p
    if p <= 1:
        return "too small"
    if (p % 4) != 1:
        return "not congruent to 1"
    k = p//4
    j = 2
    while True:
        a = powmods(j, k, p)
        b = mods(a * a, p)
        if b == -1:
            return a
        if b != 1:
            return "not prime"
        j += 1

def sq2(p):
    a = root4(p)
    return ggcd((p,0),(a,1))

n=1700915129667195972895306747621172339223172447368434887800097916055770689

p= 959955187689994468839793
q=1102161658487895451736177
r=1607631049141134793054049
p1,p2= sq2(p)
q1,q2= sq2(q)
r1,r2= sq2(r)
y=p1*q1*r2+p2*q2*r2-p1*q2*r1+p2*q1*r1
x=p1*q1*r1+p2*q2*r1+p1*q2*r2-p2*q1*r2
print(x,y)



