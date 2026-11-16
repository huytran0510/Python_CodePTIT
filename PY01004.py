from math import *


def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
while t > 0:
    n = int(input())
    cnt = 0
    for i in range(1, n):
        if gcd(i,n) == 1:
            cnt += 1
    res = 'YES' if prime(cnt) else 'NO'
    print(res)
    t -= 1