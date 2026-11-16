class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao

    def __add__(self, other):
        return SoPhuc(self.thuc + other.thuc, self.ao + other.ao)

    def __mul__(self, other):
        return SoPhuc(self.thuc * other.thuc - self.ao * other.ao, self.thuc * other.ao + self.ao * other.thuc)

    def __str__(self):
        if self.ao >= 0:
            return f"{self.thuc} + {self.ao}i"
        else:
            return f"{self.thuc} - {abs(self.ao)}i"


for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    A = SoPhuc(a, b)
    B = SoPhuc(c, d)
    tong = A + B
    C = tong * A
    D = tong * tong
    print(f"{C}, {D}")