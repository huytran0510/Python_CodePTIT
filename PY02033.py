s = input()
res = set()
for i in range(0, len(s) - 1, 2):
    x = int(s[i : i + 2])
    if x not in res:
        res.add(x)
        print(x, end=' ')