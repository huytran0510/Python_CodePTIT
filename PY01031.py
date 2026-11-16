t = int(input())
while t > 0:
    n,b = map(int, input().split())
    f = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = ""
    while n > 0:
        x = n % b
        s = f[x] + s
        n //= b
    print(s)
    t -= 1


