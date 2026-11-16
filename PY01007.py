t = int(input())
while t > 0:
    n,x,m = map(float, input().split())
    res = 0
    while n <= m:
        n = n * (1 + x/100)
        res += 1
    print(res)
    t -= 1

