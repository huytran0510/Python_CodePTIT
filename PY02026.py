n,m = map(int, input().split())
l1 = set(map(int, input().split()))
l2 = set(map(int, input().split()))
check = 1
a = list(l1)
b = list(l2)
if len(a) != len(b):
    check = 0
for i in range(len(a)):
    if a[i] != b[i]:
        check = 0
        break
res = 'YES' if check == 1 else 'NO'
print(res)

