n = int(input())
s1 = 0
for i in range(n - 1):
    x = int(input())
    s1 += x
s2 = (n * (n + 1)) // 2
print(s2 - s1)