def check(s):
    se = set()
    for i in s:
        se.add(i)
    if len(se) != 2:
        return False
    for i in range(2, len(s)):
        if s[i] != s[i-2]:
            return False
    return True

t = int(input())
while t > 0:
    s = input()
    if check(s):
        print('YES')
    else:
        print('NO')
    t -= 1
