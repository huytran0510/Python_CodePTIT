class matrix:
    def __init__(self,n,m,data):
        self.n = n
        self.m = m
        self.data = data

    def chuyen_vi(self):
        new_matrix = []
        for i in range(self.m):
            row = []
            for j in range(self.n):
                row.append(self.data[j][i])
            new_matrix.append(row)

        res = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                sum = 0
                for k in range(self.m):
                    sum += self.data[i][k] * new_matrix[k][j]
                row.append(sum)
            res.append(row)

        return res

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    mt = []
    for i in range(n):
        row = list(map(int, input().split()))
        mt.append(row)

    Mat = matrix(n,m,mt)
    res_mt = Mat.chuyen_vi()
    for row in res_mt:
        for so in row:
            print(so, end = ' ')
        print()