import math

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def palindrome(n):
    tmp = 0
    m = n
    while n > 0:
        tmp = tmp * 10 + n % 10
        n //= 10
    return m == tmp

def check(n):
    while n > 0:
        digit = n % 10
        if digit == n % 10:
            return False
    n //= 10
    return True

t = int(input())
while t > 0:
    n = int(input())
    for i in range(2, n):
        if prime(i) or check(i) or prime(palindrome(i)):
            print(i, end=' ')
    print()
    t -= 1