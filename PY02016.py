t = int(input())
while t > 0:
    n = int(input())
    l = list(map(int, input().split()))
    d = {}
    res = 0
    check = 0
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for key, val in d.items():
        if val > n/2:
            check = 1
            res = key
    if check:
        print(res)
    else:
        print('NO')
    t -= 1

