
# Calculate ab mod c. (1 ≤ a, c ≤ 2000000000). (1 ≤ b ≤ 2000000000000000)

# Input
# The input consists of a single line that has the 3 numbers a,b & c respectively.

# Output
# The output should consist of a single number, the result of the operation ab mod c.

# Example
# input
# 3 2 5
# output
# 4
def numPowerMod(a,b,c):
    b = bin(b)[2:]
    res =  1
    for i in b:
        if i == '1':
            res = ((res**2)*a)%c
        else:
            res = (res**2)%c
    return res

x = input()
a,b,c = x.split(' ')
print(numPowerMod(int(a),int(b),int(c)))
