class ThongTin:
    def __init__(self, ms, ten, mxt, p1, p2):
        self.ms = ms
        self.ten = ten
        self.mxt = mxt
        self.p1 = p1
        self.p2 = p2
        self.tong = p1*2 + p2
        self.mon = ""
        self.loai = ""
        self.diem()
        self.subject()
        self.rank()

    def diem(self):
        if self.mxt[1] == '1':
            self.tong += 2.0
        elif self.mxt[1] == '2':
            self.tong += 1.5
        elif self.mxt[1] == '3':
            self.tong += 1.0

    def subject(self):
        if self.mxt[0] == 'A':
            self.mon = 'TOAN'
        elif self.mxt[0] == 'B':
            self.mon = 'LY'
        elif self.mxt[0] == 'C':
            self.mon = 'HOA'

    def rank(self):
        if self.tong >= 18:
            self.loai = 'TRUNG TUYEN'
        else:
            self.loai = 'LOAI'
    def output(self):
        print(f"{self.ms} {self.ten} {self.mon} {self.tong} {self.loai}")


n = int(input())
l = []
cnt = 0
for _ in range(1, n + 1):
    ten = input()
    mxt = input()
    p1 = float(input())
    p2 = float(input())
    cnt += 1
    if cnt <= 9:
        ms = 'GV0' + str(cnt)
    else:
        ms = 'GV' + str(cnt)
    l.append(ThongTin(ms, ten, mxt, p1, p2))
l.sort(key = lambda x : x.tong, reverse=True)
for x in l:
    x.output()


