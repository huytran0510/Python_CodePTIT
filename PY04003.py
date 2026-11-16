from math import *
n,m = map(int, input().split())
x = gcd(n,m)
n //= x
m //= x
print(f"{n}/{m}")