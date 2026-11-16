n = int(input())
l = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if l[i] > l[j]:
            cnt += 1
print(cnt)