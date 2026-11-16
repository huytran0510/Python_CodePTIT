class ThiSinh:
    def __init__(self, ten, ns, p1, p2, p3):
        self.ten = ten
        self.ns = ns
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.res = self.p1 + self.p2 + self.p3
    def output(self):
        print(f"{self.ten} {self.ns} {self.res}")

ten = input()
ns = input()
p1 = float(input())
p2 = float(input())
p3 = float(input())
ThiSinh(ten, ns, p1, p2, p3).output()


