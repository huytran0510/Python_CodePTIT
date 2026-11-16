with open ("DATA.in", "r") as f:
    text = f.read().split()
l = []
for i in text:
    if i.isdigit():
        if int(i) < -(2**31) or int(i) > (2**31):
            l.append(i)
    else:
        l.append(i)
print(*sorted(l))
