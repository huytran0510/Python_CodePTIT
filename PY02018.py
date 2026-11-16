n = int(input())
l = list(map(int, input().split()))
d = {}
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in range(1, n + 2):
    if i not in d:
        print(i)
        break