def check(s):
    return s == s[::-1]

with open ("VANBAN.in", "r") as f:
    text = f.read().split()
l = []
max_val = 0
for x in text:
    if check(x):
        l.append(x)
        max_val = max(len(x), max_val)
d = {}
for x in l:
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1
for x,y in d.items():
    if len(x) == max_val:
        print(x,y)


