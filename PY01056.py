from math import *

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(s):
    res = 0
    for i in range(len(s)):
        if i % 2 == 0 and int(s[i]) % 2 != 0:
            return False
        if i % 2 != 0 and int(s[i]) % 2 == 0:
            return False
        res += int(s[i])
    return prime(res)

t = int(input())
while t > 0:
    s = input().strip()
    if (check(s)):
        print('YES')
    else:
        print('NO')
    t -= 1

