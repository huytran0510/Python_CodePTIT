t = int(input())
while t > 0:
    test = int(input())
    d = {}
    while test > 0:
        n = int(input())
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
        test -= 1
    res = m = 0
    for x,y in d.items():
        if y > m:
            m = y
            res = x
        elif y == m:
            if x < res:
                res = x
    print(res)
    t -= 1




