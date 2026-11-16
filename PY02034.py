s = input()
res = {}
for i in range(0, len(s) - 1, 2):
    x = int(s[i : i + 2])
    if x not in res:
        res[x] = 1
    else:
        res[x] += 1
for a,b in res.items():
    print(a,b)


