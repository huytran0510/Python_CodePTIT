t = int(input())
while t > 0:
    s = input().strip()
    res = 1
    for c in s:
        if c == '0':
            continue
        else:
            res *= int(c)
    print(res)
    t -= 1
