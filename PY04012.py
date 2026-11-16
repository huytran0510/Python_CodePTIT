class SinhVien:
    def __init__(self, msv, ten, lop):
        self.msv = msv
        self.ten = ten
        self.lop = lop
        self.diem = 10
        self.ghichu = ''
    def Point(self, s):
        for c in s:
            if c == 'v':
                self.diem -= 2
            elif c == 'm':
                self.diem -= 1
        if self.diem <= 0:
            self.diem = 0
            self.ghichu = 'KDDK'
    def output(self):
        print(f"{self.msv} {self.ten} {self.lop} {self.diem} {self.ghichu}")

n = int(input())
l = []
for _ in range(n):
    msv = input()
    ten = input()
    lop = input()
    sv = SinhVien(msv, ten, lop)
    l.append(sv)
for _ in range(n):
    s = input().split()
    msv_input = s[0]
    diem_danh = s[1]
    for sv in l:
        if sv.msv == msv_input:
            sv.Point(diem_danh)
for x in l:
    x.output()


