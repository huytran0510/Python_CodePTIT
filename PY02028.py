from math import *

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
l = list(map(int, input().split()))
res = list()
cnt = 0
for i in l:
    if prime(i):
        res.append(i)
res.sort()
for i in l:
    if i in res:
        print(res[cnt], end=' ')
        cnt += 1
    else:
        print(i, end= ' ')
