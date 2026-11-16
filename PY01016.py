t = int(input())
while t > 0:
    s = input()
    res = ''
    for i in range(0, len(s), 2):
        c = s[i]
        k = int(s[i + 1])
        res += c * k
    print(res)
    t -= 1

