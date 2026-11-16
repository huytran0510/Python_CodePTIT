class ThongTin:
    def __init__(self, ma, ten, sl, don_gia, ckhau):
        self.ma = ma
        self.ten = ten
        self.sl = sl
        self.don_gia = don_gia
        self.ckhau = ckhau
        self.tong = self.sl * self.don_gia - self.ckhau
    def output(self):
        print(f"{self.ma} {self.ten} {self.sl} {self.don_gia} {self.ckhau} {self.tong}")

n = int(input())
l = []
for i in range(1, n + 1):
    ma = input()
    ten = input()
    sl = int(input())
    don_gia = int(input())
    ck = int(input())
    l.append(ThongTin(ma, ten, sl, don_gia, ck))
l.sort(key = lambda x : x.tong, reverse=True)
for x in l:
    x.output()

