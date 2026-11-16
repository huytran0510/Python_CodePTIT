t,k = map(int, input().split())
l = []
d = {}
for _ in range(t):
    s = input()
    text = ''
    for c in s:
        if c.isalnum():
            text += c.lower()
        else:
            text += " "
    for i in text.split():
        l.append(i)
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
l1 = list(d.items())
l1.sort(key = lambda x : (-x[1], x[0]))
for x,y in l1:
    if y >= k:
        print(x,y)


