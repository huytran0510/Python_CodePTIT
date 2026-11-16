import math

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
l = list(map(int, input().split()))
fre = {}

for i in l:
    if i in fre:
        fre[i] += 1
    else:
        if prime(i):
            fre[i] = 1

for i in l:
    if prime(i) and fre[i] > 0:
        print(f'{i} {fre[i]}')
        fre[i] = 0

