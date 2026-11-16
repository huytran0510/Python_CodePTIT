import sys

input_data = sys.stdin.read().split()

if input_data:
    n = int(input_data[0])

    a = [int(x) for x in input_data[1:]]

    even = []
    odd = []

    for x in a:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)

    even.sort()
    odd.sort(reverse=True)

    count1 = 0
    count2 = 0
    res = []

    for x in a:
        if x % 2 == 0:
            res.append(even[count1])
            count1 += 1
        else:
            res.append(odd[count2])
            count2 += 1

    print(*res)