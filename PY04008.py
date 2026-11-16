import sys

class Matrix:
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
                tong = 0
                for k in range(self.m):
                    tong += self.data[i][k] * new_matrix[k][j]
                row.append(tong)
            res.append(row)

        return res

input_data = sys.stdin.read().split()
if input_data:
    t = int(input_data[0])
    idx = 1
    for _ in range(t):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        idx += 2
        mtx = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(int(input_data[idx]))
                idx += 1
            mtx.append(row)
        new_mtx = Matrix(n,m, mtx)
        res_new_mtx = new_mtx.chuyen_vi()
        for x in res_new_mtx:
            for y in x:
                print(y, end=  ' ')
            print()



