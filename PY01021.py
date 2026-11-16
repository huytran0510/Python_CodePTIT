t = int(input())
while t > 0:
    s = input().strip()
    char = []
    num = []
    for c in s:
        if c.isdigit():
            num.append(int(c))
        else:
            char.append(c)
    char.sort()
    res = ''
    for i in char:
        res += i
    res += str(sum(num))
    print(res)
    t -= 1
