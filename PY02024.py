def cmp(s):
    res = 1
    for i in s:
        res *= int(i)
    return (res, int(s))

t = int(input())
while t > 0:
    n = int(input())
    s = input().split()
    s.sort(key = cmp)
    for i in s:
        print(i, end = ' ')
    print()
    t -= 1