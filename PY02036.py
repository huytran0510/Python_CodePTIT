from math import *

n = int(input())
l = list(map(int, input().split()))
l.sort()
for i in range(n):
    for j in range(1, n):
        if gcd(l[i], l[j]) == 1 and l[i] < l[j]:
            print(f"{l[i]} {l[j]}")
