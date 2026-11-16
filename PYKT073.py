import sys

input_data = sys.stdin.readlines()
if input_data:
    idx = 1
    length = []
    t = int(input_data[0])
    for _ in range(t):
        s = input_data[idx].split()
        length.append(len(s))
        idx += 1
    res = []
    cnt = 0
    while cnt < len(length):
        if length[cnt] == 7:
            res.append(2)
            cnt += 4
        elif length[cnt] == 6:
            res.append(1)
            while cnt < len(length) and (length[cnt] == 6 or length[cnt] == 8):
                cnt += 1
    print(len(res))
    for x in res:
        print(x)


