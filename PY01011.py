def check(s):
    if s != s[::-1]:
        return False
    if len(s) % 2 != 0:
        return False
    for c in s:
        if int(c) % 2 != 0:
            return False
    return True

t = int(input())
while t > 0:
    n = int(input())
    for i in range(22, n):
        if check(str(i)):
            print(i, end = ' ')
    print()
    t -= 1