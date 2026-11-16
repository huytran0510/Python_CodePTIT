n = int(input(), 2)
f = "0123456789ABCDEFGHIJKLMNOPQRSTUVWSYZ"
s = ''
while n > 0:
    x = n % 8
    s = f[x] + s
    n //= 8
print(s)
