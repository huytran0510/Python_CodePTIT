s = input()
n = int(input())
d = {}
for i in range(0, len(s) - 1, 2):
    x = int(s[i: i + 2])
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1
check = 0
for x,y in d.items():
    if y >= n:
        check = 1
if check == 1:
    for x,y in sorted(d.items()):
        if y >= n:
            print(x,y)
else:
    print('NOT FOUND')

