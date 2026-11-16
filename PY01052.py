from math import *

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum(n):
    res = 0
    for c in n:
        res += int(c)
    return res

t = int(input())
while t > 0:
    s = input().strip()
    if prime(sum(s)):
        print('YES')
    else:
        print('NO')
    t -= 1

