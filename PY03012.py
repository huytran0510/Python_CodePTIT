n = int(input())
l = []
for i in range(n):
    s = input()
    c,t = map(int, input().split())
    l.append((s,c,t))
l.sort(key= lambda x : (-x[1], x[2], x[0]))
for i in l:
    print(*i)
