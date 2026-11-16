from itertools import permutations
from math import factorial

t = int(input())
for _ in range(t):
    n = int(input())
    arr = (str(i) for i in range(n , 0, -1))
    print(factorial(n))
    for x in permutations(arr):
        print("".join(x), end = ' ')
    print()
