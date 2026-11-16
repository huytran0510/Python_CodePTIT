import  sys

def check(s):
    s = s.split(".")
    if len(s) != 4:
        return False
    for x in s:
        if not x.isdigit():
            return False
        else:
            if int(x) < 0 or int(x) > 255:
                return False
    return True

input_data = sys.stdin.read().split()
if input_data:
    t = int(input_data[0])
    idx = 1
    for _ in range(t):
        ip = input_data[idx]
        idx += 1
        print("YES" if check(ip) else "NO")

