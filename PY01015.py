def check(s):
    for i in range(1, len(s)):
        if s[i] < s[i - 1]:
            return "NO"
    return "YES"

t = int(input())
while t > 0:
    s = input().strip()
    print(check(s))
    t -= 1