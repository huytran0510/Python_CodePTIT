from math import *

t = int(input())
while t > 0:
    s = input().strip()
    if gcd(int(s), int(s[::-1])) == 1:
        print('YES')
    else:
        print('NO')
    t -= 1