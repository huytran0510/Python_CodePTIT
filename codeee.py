import numpy as np

# 1. Khởi tạo 2 vector dạng Cột (Column Vector)
# Đây là chuẩn mực khi lưu trữ dữ liệu
w = np.array([[200],
              [10],
              [50]])  # Shape: (3, 1)

x = np.array([[2],
              [5],
              [3]])   # Shape: (3, 1)

print(f"Shape của w: {w.shape}")
print(f"Shape của x: {x.shape}")

# ---------------------------------------------------------
# TRƯỜNG HỢP 1: Nhân bừa (Không Transpose) -> Sẽ lỗi hoặc ra sai
try:
    # np.dot là lệnh nhân ma trận
    wrong_result = np.dot(w, x)
except ValueError as e:
    print("\n❌ LỖI RỒI: ", e)
    print("Giải thích: Đuôi thằng w (1) không khớp đầu thằng x (3)")

# ---------------------------------------------------------
# TRƯỜNG HỢP 2: Có Transpose (Lật w nằm ngang) -> Chuẩn bài
# w.T biến shape (3, 1) thành (1, 3)
correct_result = np.dot(w.T, x)

print("\n✅ KẾT QUẢ ĐÚNG:")
print(f"Shape của w.T: {w.T.shape}")
print(f"Phép tính: (1, 3) nhân (3, 1) -> Ra (1, 1)")
print(f"Tổng tiền: {correct_result[0][0]}k")






class SieuNhan:
    suc_manh = 36
    stt = 1
    so_thu_tu = 1
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = "Sieu nhan " + para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
        self.stt = SieuNhan.so_thu_tu
        SieuNhan.so_thu_tu += 1
    def xinchao(self):
        return 'Xin chao, toi la ' + self.ten

sieu_nhan_a = SieuNhan('huy', 'kiem', 'xanh')
sieu_nhan_b = SieuNhan('huy', 'kiem', 'xanh')
print(sieu_nhan_a.stt)
print(sieu_nhan_b.stt)


import sys

data = sys.stdin.read().split()

idx = 0
t = int(data[idx])
idx += 1

for _ in range(t):
    n = int(data[idx])
    m = int(data[idx+1])
    idx += 2

    l = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(data[idx]))
            idx += 1
        l.append(row)

    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(m):
                res[i][j] += l[i][k] * l[j][k]
    for row in res:
        print(' '.join(map(str, row)))