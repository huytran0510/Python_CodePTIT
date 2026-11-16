import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, k):
        return math.sqrt((self.x - k.x ) ** 2 + (self.y - k.y ) ** 2)

class Triangle:
    def __init__(self, p1, p2, p3):
        self.a = p1.distance(p2)
        self.b = p2.distance(p3)
        self.c = p3.distance(p1)
    def check(self):
        a,b,c = self.a, self.b, self.c
        return a + b > c and b + c > a and a + c > b
    def peri(self):
        return self.a + self.b + self.c

t = int(input())
l = []
for _ in range(t):
    l += list(map(float, input().split()))
i = 0
for _ in range(t):
    p1 = Point(l[i], l[i + 1])
    p2 = Point(l[i + 2], l[i + 3])
    p3 = Point(l[i+4] , l[i + 5])
    Tri = Triangle(p1, p2, p3)
    if Tri.check():
        print(f"{Tri.peri():.6f}")
    else:
        print('INVALID')
    i += 6




