from math import *

def check(s):
    sum = 0
    for c in s:
        sum += int(c)
    return sum % 10 == 0

def dis(s):
    for i in range(len(s) - 1):
        if abs(int(s[i]) - int(s[i+1])) != 2:
            return False
    return True

t = int(input())
while t > 0:
    s = input().strip()
    if check(s) and dis(s):
        print('YES')
    else:
        print('NO')
    t -= 1
