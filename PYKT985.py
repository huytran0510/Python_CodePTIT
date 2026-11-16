import sys

input_data = sys.stdin.read().splitlines()[1:]
res = []
t = 1

for x in input_data:
    if not x.strip():
        t = 1
    elif t == 1:
        res.append([x,0])
        t = 0
    else:
        res[-1][1] += 1

for x,y in res:
    print(f"{x}: {y}")




