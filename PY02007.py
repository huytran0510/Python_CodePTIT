import sys
num = sys.stdin.read().split()
s = set()
for i in num:
    res = int(i) % 42
    s.add(res)
print(len(s))
