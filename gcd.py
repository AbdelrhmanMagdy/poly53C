
# Assume you are working in mod(M) arithmetic, what is the additive and multiplicative inverse of N?

# Input
# The input consists of 1 line that has 2 numbers M, N respectively (1 ≤ M, N ≤ 20000000000000000000000)

# Output
# In case N has no multiplicative inverse, print "IMPOSSIBLE" without the quotes. Otherwise print 2 numbers which represent the additive and multiplicative inverses respectively of N. All printed numbers must be mod(M)
# input
# 3 2
# output
# 1 2
# input
# 6 3
# output
# IMPOSSIBLE
def gcd(s,g):
    if s>g:
        s,g=g,s
    while not s == 0:
        temp = g
        g = s
        s = temp%s
    return g

def euclid(a3,b3):
    if not gcd(b3,a3) == 1:
        print('IMPOSSIBLE')
        return
    a1,a2,b1,b2 = 1,0,0,1
    mod = a3
    n = b3
    while not b3 == 1:
        q = int(a3/b3)
        t1,t2,t3 = a1,a2,a3
        a1,a2,a3 = b1,b2,b3
        b1,b2,b3 = (t1-q*a1),(t2-q*a2),(t3-q*a3)
    print((-n+mod)%mod,b2 % mod)

x = input()
a3,b3 = x.split(' ')
euclid(int(a3),int(b3))
