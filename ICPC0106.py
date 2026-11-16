t = int(input())
for _ in range(t):
    b = int(input())
    n = int(input(), 2)
    f = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        x = n % b
        res = f[x] + res
        n //= b
    print(res)

