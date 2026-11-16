s = input().strip()
cnt_h = cnt_t = 0
for c in s:
    if c.isupper():
        cnt_h += 1
    else:
        cnt_t += 1
if cnt_h > cnt_t:
    print(s.upper())
else:
    print(s.lower())