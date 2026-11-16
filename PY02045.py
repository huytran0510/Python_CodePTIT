s = input()
while len(s) > 1:
    m = len(s) // 2
    n1 = int(s[0 : m])
    n2 = int(s[m:])
    res = n1 + n2
    s = str(res)
    print(s)


