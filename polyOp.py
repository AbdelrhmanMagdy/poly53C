
# Given 2 numbers in Hex format that represent 2 polynomials in GF(28) with m(x) = x8 + x4 + x3 + x + 1. Find the result of Adding and Multiplying those numbers. Note: Result of addition is the same as the result of subtraction.

# Input
# The input consists of 1 line that has 2 numbers, each of which consists of 2 Hex digits that represent the 2 given numbers as described above.

# Output
# In a single line print 2 numbers in Hex format(All characters must be capital), the first one should be the result of the addition of the given 2 numbers and the second is the result of multiplying them. These operations should be done in GF(28) with m(x) = x8 + x4 + x3 + x + 1.

# Example
# input
# 01 01
# output
# 00 01
# GF(2^8)
def hex2bin(hex):
    return (bin(int(hex, 16))[2:]).zfill(len(hex)*4)

def bin2hex(bin):
    return hex(int(''.join(bin), 2)).upper()[2:].zfill(int(len(bin)/4))

def xorHex(p1,p2):
    res = int(hex2bin(p1),2)^int(hex2bin(p2),2)
    return bin2hex('{0:b}'.format(res)).zfill(len(p1))
def shiftLeftXBit(p1,x):
    mx = '1B'
    for i in range(x):
        if hex2bin(p1)[0] == '1':
            p1 = hex2bin(p1)[1:]+'0'
            p1 = xorHex(bin2hex(p1), mx)
        else:
            p1 = bin2hex(hex2bin(p1)[1:]+'0')
    return p1
    
def polyMult(p1,p2):
    index = 0
    res = '00'
    for i in reversed(list(hex2bin(p2))):
        if i == '1':
            res = xorHex(res, shiftLeftXBit(p1,index))
        index += 1
    return res

x = input()
p1, p2 = x.split(' ')
print(xorHex(p1,p2),polyMult(p1,p2))