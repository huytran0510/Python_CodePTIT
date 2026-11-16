from math import *
a,b,x,y = map(int, input().split())
tu = a * y + b * x
mau = b * y
c = gcd(tu, mau)
tu //= c
mau //= c
print(f"{tu}/{mau}")