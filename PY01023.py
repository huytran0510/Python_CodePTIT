from math import *

t = int(input())
while t > 0:
    n = int(input())
    print('1 * ', end = '')
    for i in range(2, int(sqrt(n)) + 1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
        if (cnt > 0):
            print(f"{i}^{cnt}", end = ' ')
            if (n > 1):
                print('*', end= ' ')

    if n > 1 :
        print(f"{n}^1", end = ' ')
    print()
    t -= 1