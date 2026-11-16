def point(n):
    if 3 <= n <= 4:
        return 2.5
    elif 5 <= n <= 6:
        return 3.0
    elif 7 <= n <= 9:
        return 3.5
    elif 10 <= n <= 12:
        return 4.0
    elif 13 <= n <= 15:
        return 4.5
    elif 16 <= n <= 19:
        return 5.0
    elif 20 <= n <= 22:
        return 5.5
    elif 23 <= n <= 26:
        return 6.0
    elif 27 <= n <= 29:
        return 6.5
    elif 30 <= n <= 32:
        return 7.0
    elif 33 <= n <= 34:
        return 7.5
    elif 35 <= n <= 36:
        return 8.0
    elif 37 <= n <= 38:
        return 8.5
    elif 39 <= n <= 40:
        return 9.0


t = int(input())
while t > 0:
    x = input().split()
    r, l = int(x[0]), int(x[1])
    s, w = float(x[2]), float(x[3])
    r = point(r)
    l = point(l)
    res = (l + r + w + s) / 4.0
    if res - int(res) >= 0.75:
        print(int(res) + 1.0)
    elif res - int(res) >= 0.25:
        print(int(res) + 0.5)
    else:
        print(float(int(res)))
    t -= 1

