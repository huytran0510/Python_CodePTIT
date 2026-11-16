def sum(s):
    res = 0
    for c in s:
        res += int(c)
    return res

def check(s):
    if len(s) <= 1 or s != s[::-1]:
        return False
    return True

t = int(input())
while t > 0:
    s = input().strip()
    if check(str(sum(s))):
        print('YES')
    else:
        print('NO')
    t -= 1

