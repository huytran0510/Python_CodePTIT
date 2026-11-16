n = int(input())
l = list(map(int, input().split()))
res = []
l.sort()
res.append(l[n-1] * l[n-2] * l[n-3])
res.append(l[0] * l[1] * l[n-1])
res.append(l[0] * l[1])
res.append(l[n-1] * l[n-2])
print(max(res))