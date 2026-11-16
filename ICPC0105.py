t = int(input())
while t > 0:
    s = input().strip()
    res = ''
    for c in s:
        if c.isdigit():
            res += c
        else:
            res += ' '
    l = res.split()
    nums = list(map(int, l))
    print(max(nums))
    t -= 1

