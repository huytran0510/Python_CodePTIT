class MonThi:
    def __init__(self, ma, ten, hinh_thuc):
        self.ma = ma
        self.ten = ten
        self.ht = hinh_thuc
    def output(self):
        print(f"{self.ma} {self.ten} {self.ht}")

t = int(input())
l = []
for _ in range(t):
    ma = input()
    ten = input()
    hinhthuc = input()
    l.append(MonThi(ma, ten, hinhthuc))
l.sort(key= lambda x : (x.ma))
for x in l:
    x.output()

