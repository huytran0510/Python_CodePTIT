import sys

lines = sys.stdin.read().splitlines()[1:]

res = []
t = 1

for x in lines:
    if not x.strip():
        t = 1
    elif t == 1:
        res.append([x, 0])
        t = 0
    else:
        res[-1][1] += 1

# In kết quả
for k, v in res:
    print(f"{k}: {v}")

# 9
# Home / accommodation
# What kind of housing / accommodation do you live in?
# Who do you live with?
# How long have you lived there?
#
#
# Study
# Describe your education
# What is your area of specialization?
# Why did you choose to study that major?