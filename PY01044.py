s1 = set(input().lower().split())
s2 = set(input().lower().split())
res1 = s1 | s2
res2 = s1 & s2
print(*sorted(res1))
print(*sorted(res2))

