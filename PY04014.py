class HocSinh:
    def __init__(self, ms, ten, d):
        self.ms = ms
        self.ten = ten
        self.p1 = d[0]
        self.p2 = d[1]
        self.p3 = d[2]
        self.p4 = d[3]
        self.p5 = d[4]
        self.p6 = d[5]
        self.p7 = d[6]
        self.p8 = d[7]
        self.p9 = d[8]
        self.p10 = d[9]
        self.tong = (self.p1 * 2 + self.p2 * 2 + self.p3 + self.p4 + self.p5 + self.p6 + self.p7 + self.p8 + self.p9 + self.p10) / 10 / 1.2
        self.loai = ''
        self.rank()
    def rank(self):
        if self.tong < 5:
            self.loai =  'YEU'
        elif 5 <= self.tong <= 6.9:
            self.loai = 'TB'
        elif 7 <= self.tong <= 7.9:
            self.loai = 'KHA'
        elif 8 <= self.tong <= 8.9:
            self.loai = 'GIOI'
        else:
            self.loai = 'XUAT SAC'
    def output(self):
        print(f"{self.ms} {self.ten} {self.tong:.1f} {self.loai}")

n = int(input())
l = []
cnt = 0
for _ in range(1, n + 1):
    ten = input()
    d = list(map(float, input().split()))
    cnt += 1
    if cnt <= 9:
        ms = 'HS0' + str(cnt)
    else:
        ms = 'HS' + str(cnt)
    l.append(HocSinh(ms, ten, d))
l.sort(key = lambda x : (-x.tong, x.ms))
for x in l:
    x.output()


