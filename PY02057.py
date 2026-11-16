n,m = map(int, input().split())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    
min_val = min(min(row) for row in matrix)
max_val = max(max(row) for row in matrix)
res = max_val - min_val

check = False
for i in range(n):
    for j in range(m):
        if matrix[i][j] == res:
            check = True
            
if check:
    print(res)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == res:
                print(f"Vi tri [{i}][{j}]")
else: print('NOT FOUND')
