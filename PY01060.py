t = int(input())
while t > 0:
    s = input().strip()
    res1 = 0
    res2 = 1
    cnt = 0
    for i in range(1, len(s), 2):
        res1 += int(s[i])
    for i in range(0, len(s), 2):
        if s[i] != '0':
            res2 *= int(s[i])
            cnt += 1
    if cnt == 0:
        res2 = 0
    print(f"{res2} {res1}")
    t -= 1


