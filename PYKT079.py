t = int(input())
while t > 0:
    n = int(input())
    l = list(map(int, input().split()))
    a = min(l)
    b = max(l)
    d = {}
    res = []
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in range(a, b + 1):
        if i not in d:
            res.append(i)
    print(len(res))
    t -= 1
