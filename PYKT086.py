with open ("DATA.in", "r") as f:
    text = f.read().split()
t = int(text[0])
idx = 1
for _ in range(t):
    b = int(text[idx])
    n = int(text[idx + 1], 2)
    f = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = ""
    while n > 0:
        x = n % b
        s = f[x] + s
        n //= b
    print(s)
    idx += 2

