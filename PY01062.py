import math

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(s):
    if not prime(len(s)):
        return False
    cnt1 = cnt2 = 0
    for c in s:
        if prime(int(c)):
            cnt1 += 1
        else:
            cnt2 += 1
    return cnt1 > cnt2

t = int(input())
while t > 0:
    n = input().strip()
    res = 'YES' if check(n) else 'NO'
    print(res)
    t -= 1

