from itertools import permutations

s = input().strip()
for x in permutations(s):
    print("".join(x))