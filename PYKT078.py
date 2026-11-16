t = int(input())
while t > 0:
    n,m = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    max_i = l.index(max(l))
    l.insert(max_i - 1, m)
    print(*l)
    t -= 1


