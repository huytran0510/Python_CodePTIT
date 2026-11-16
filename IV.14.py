s = input()
l = s.split()
res = max(l, key = len)
print(res, len(res))

