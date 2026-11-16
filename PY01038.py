t = int(input())
for _ in range(t):
    n = int(input())
    if n % 7 == 0:
        print(n)
        continue
    check = False
    for i in range(1000):
        tmp = int(str(n)[::-1])
        n = n + tmp
        if n % 7 == 0:
            print(n)
            check = True
            break
    if not check:
        print(-1)
