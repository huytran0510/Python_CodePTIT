while True:
    n = int(input())
    if n == 0:
        break
    l = []
    for i in range(n):
        l.append(int(input()))
    if max(l) != min(l):
        print(f"{min(l)} {max(l)}")
    else:
        print('BANG NHAU')


