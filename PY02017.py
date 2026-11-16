t = int(input())
while t > 0:
    n = int(input())
    l = list(map(int, input().split()))
    cnt = {}
    for i in l:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    for fi, se in cnt.items():
        if se % 2 != 0:
            print(fi)
            break
    t -= 1


