a,k,n = map(int, input().split())
start = k - (a % k)
res = list(range(start, n - a + 1, k))
if res:
    print(*res)
else:
    print('-1')
