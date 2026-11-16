from math import *

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum(s):
    res = 0
    for c in s:
        res += int(c)
    return res

def check(s):
    if not prime(int(s)) and not prime(int(s[::-1])) and not prime(sum(s)):
        return False
    for c in s:
        if not prime(int(c)):
            return False
    return True

t = int(input())
while t > 0:
    s = input().strip()
    res = 'Yes' if check(s) else 'No'
    print(res)
    t -= 1


