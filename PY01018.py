while True:
    line = input().split()
    k = int(line[0])
    if k == 0:
        break
    s = line[1]
    p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    res = ""
    for c in s:
        i = p.find(c)
        res += p[(i + k) % 28]
    print(res[::-1])
