class NhanVien:
    def __init__(self, ma, ten, tb):
        self.ma = ma
        self.ten = ten
        self.tb = tb
        if self.tb < 5:
            self.loai = "TRUOT"
        elif self.tb < 8:
            self.loai = "CAN NHAC"
        elif self.tb <= 9.5:
            self.loai = "DAT"
        else:
            self.loai = "XUAT SAC"

    def output(self):
        return f"{self.ma} {self.ten} {self.tb:.2f} {self.loai}"

n = int(input())
l = []

for i in range(1, n + 1):
    ten = input().strip()
    p1 = float(input())
    p2 = float(input())
    if p1 > 10: p1 /= 10.0
    if p2 > 10: p2 /= 10.0
    dtb = (p1 + p2) / 2.0
    ms = "TS0" + str(i)
    l.append(NhanVien(ms, ten, dtb))
l.sort(key=lambda x: x.tb, reverse=True)
for x in l:
   print(x.output())