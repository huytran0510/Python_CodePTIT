from math import *

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n,m = map(int, input().split())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

res = -1
for i in range(n):
    for j in range(m):
        if prime(matrix[i][j]):
            res = max(res, matrix[i][j])
if res == -1:
    print('NOT FOUND')
else:
    print(res)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == res:
                print(f"Vi tri [{i}][{j}]")