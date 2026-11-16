from math import *

# def check(n, mtx):
#     for i in range(n):
#         if mtx[i][i] != mtx[0][0]:
#             return False
#         for j in range(n):
#             if mtx[i][j] != mtx[j][i]:
#                 return False
#     return True
#
# n = int(input())
# mt = []
# for i in range(n):
#     row = list(map(int, input().split()))
#     mt.append(row)
# print("YES" if check(n, mt) else "NO")


# class ThiSinh:
#     def __init__(self,ten,ns,p1,p2,p3):
#         self.ten = ten
#         self.ns = ns
#         self.p1 = p1
#         self.p2 = p2
#         self.p3 = p3
#         self.tong = self.p1 + self.p2 + self.p3
#         self.min = min(self.p1, self.p2, self.p3)
#         self.dtb = (self.tong + self.min) / 4.0
#
#     def output(self):
#         print(f"{self.ten} {self.ns} {self.dtb:.1f}")
#
# n = int(input())
# l = []
# for _ in range(n):
#     ten = input()
#     ns = input()
#     p1 = float(input())
#     p2 = float(input())
#     p3 = float(input())
#     l.append(ThiSinh(ten, ns, p1, p2, p3))
# l.sort(key = lambda x : (-x.dtb))
# for x in l:
#     x.output()


# t = int(input())
# for _ in range(t):
#     n,m = map(int, input().split())
#     s1 = set(map(int, input().split()))
#     s2 = set(map(int, input().split()))
#     l1 = list(s1 & s2)
#     l2 = list(s1 | s2)
#     print("%.5f" % (len(l1) / len(l2)))
#
#
# t = int(input())
# for _ in range(t):
#     s = input()
#     res = ""
#     for i in range(len(s)):
#         if s[i] == '0':
#             res += s[i]
#         else:
#             res += " "
#     l = list(res.split())
#     if len(l) == 0:
#         print(0)
#     else:
#         print(len(max(l)))


# t = int(input())
# for _ in range(t):
#     s = input()
#     l1, l2 = [], []
#     for i in range(len(s)):
#         if i % 2 == 0:
#             l1.append(int(s[i]))
#         else:
#             l2.append(int(s[i]))
#     r1 = prod(l1)
#     r2 = sum(l2)
#     if (r2 == 0):
#         print("INVALID")
#     else:
#         res = r1 / r2
#         print("%.6f" % res)



# t = int(input())
# for _ in range(t):
#     a = [int(i) for i in input().split()]
#     b = [int(i) for i in  input().split()]
#
#     s1 = 0
#     s2 = 0
#     for i in range(len(a)):
#         s1 += (a[i] - b[i]) ** 2
#         s2 += a[i] * b[i]
#     print(f"{sqrt(s1):.2f} {s2}")


# t = int(input())
# for _ in range(t):
#     s1 = input()
#     s2 = input()
#     se1 = set(i.lower() for i in s1.split())
#     res = []
#     for i in s2.split():
#         if i.lower() in se1:
#             res.append(i)
#     print(res)


valid = []
for a in range(10, 100):
    for b in range(10, 100):
        if a + b < 100:
            valid.append(f"{a} + {b} = {a + b}")
        if a - b > 9:
            valid.append(f"{a} - {b} = {a - b}")

t = int(input())
for _ in range(t):
    s = input().replace(" ", "")
    for x in valid:
        tmp = x.replace(" ", "")
        check = True
        for i in range(len(s)):
            if s[i] != '?' and s[i] != tmp[i]:
                check = False
                break
        if check:
            print(x)
            break
    else:
        print("WRONG PROBLEM!")
