import sys

def change(a,b,s):
    return s.replace(a, b)

input_data = sys.stdin.read().split()
if input_data:
    t = int(input_data[0])
    idx = 1
    for _ in range(t):
        p = input_data[idx]
        q = input_data[idx + 1]
        s1 = input_data[idx + 2]
        s2 = input_data[idx + 3]
        idx += 4

        if p > q:
            p,q = q,p
        min_sum = int(change(q,p,s1)) + int(change(q,p,s2))
        max_sum = int(change(p,q,s1)) + int(change(p,q,s2))
        print(min_sum, max_sum)
