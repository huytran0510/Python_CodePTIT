valid = []
for a in range(10, 100):
    for b in range(10, 100):
        if a + b < 100:
            valid.append(f"{a} + {b} = {a + b}")
        if a - b > 9:
            valid.append(f"{a} - {b} = {a - b}")

t = int(input())
for _ in range(t):
    s = input().replace(" ", "")
    for x in valid:
        tmp = x.replace(" ", "")
        check = True
        for i in range(len(s)):
            if s[i] != '?' and s[i] != tmp[i]:
                check = False
                break
        if check:
            print(x)
            break
    else:
        print("WRONG PROBLEM!")