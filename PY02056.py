def check(n):
    if n < 10:
        return False
    tmp = 0
    m = n
    while n > 0:
        tmp = tmp * 10 + n % 10
        n //= 10
    return tmp == m

n,m = map(int, input().split())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
res = -1
for i in range(n):
    for j in range(m):
        if check(matrix[i][j]):
            res = max(res, matrix[i][j])
if res == -1:
    print('NOT FOUND')
else:
    print(res)
    for i in range(n):
        for j in range(m):
            if res == matrix[i][j]:
                print(f"Vi tri [{i}][{j}]")



