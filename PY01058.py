import math

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
while t > 0:
    s = input().strip()
    n = int(s[len(s) - 4 : len(s)])
    res = 'YES' if prime(n) else 'NO'
    print(res)
    t -= 1



