t = int(input())
while t > 0:
    s = input()
    check = 1
    for c in s:
        if (c != '7') and (c != '4'):
            check = 0
    if check == 1:
        print('YES')
    else:
        print('NO')
    t -= 1

