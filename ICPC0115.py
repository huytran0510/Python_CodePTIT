from math import *

t = int(input())
while t > 0:
    n = int(input())
    m = n
    sum = 0
    while n > 0:
        sum += factorial(n % 10)
        n //= 10
    res = 'Yes' if sum == m else 'No'
    print(res)
    t -= 1