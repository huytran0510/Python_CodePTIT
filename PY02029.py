n,m = map(int, input().split())
l = list(map(int, input().split()))
d = {}
mx = s = 0
res = -1
for i in l:
    if i in d:
        d[i] += 1
mx = max(d.values())
for i in range(1, m + 1):
    if d[i] != mx and d[i] > res:
        res = d[i]
        s = i
if s == 0:
    print('NONE')
else:
    print(s)

