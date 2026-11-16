t = int(input())
while t > 0:
    s = input().strip()
    res = 'YES' if s[0] == s[-1] else 'NO'
    print(res)
    t -= 1