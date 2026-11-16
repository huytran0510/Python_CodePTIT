n = int(input())
l = list(map(float, input().split()))
for i in l:
    if i == min(l):
        l.remove(i)
    elif i == max(l):
        l.remove(i)
res = sum(l) / len(l)
print('%.2f' % res)