from math import *

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) +1):
        if n % i == 0:
            return False
    return True

def sum(n):
    res = 0;
    while n > 0:
        res += (n % 10)
        n //= 10
    return res


def GCD(a,b):
    while (b != 0):
        r = a % b
        a = b
        b = r
    return a

t = int(input())
while t > 0:
    a,b = map(int, input().split())
    if prime(sum(GCD(a,b))):
        print('YES')
    else:
        print('NO')
    t -= 1