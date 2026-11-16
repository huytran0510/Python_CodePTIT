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
    s = input().strip()
    check = 1
    for i in range(0, len(s)):
        if prime(i) != prime(int(s[i])):
            check = 0
            break
    res = 'YES' if check == 1 else 'NO'
    print(res)
    t -= 1

