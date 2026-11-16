s = input()
res = set()
for i in range(0, len(s) - 1, 2):
    x = int(s[i : i + 2])
    res.add(x)
print(res)