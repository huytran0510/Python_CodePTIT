t = int(input())
while t > 0:
    n,d = map(int, input().split())
    l = list(map(int, input().split()))
    for i in range(d, n):
        print(l[i], end = ' ')
    for i in range(0, d):
        print(l[i], end = ' ')
    print("\n")
    t -= 1

