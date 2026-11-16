for i in range(int(input())):
    s1 = input().lower()
    s2 = input().lower()
    res = []

    word1 = set(s1.split())
    word2 = s2.split()
    for i in word2:
        if i in word1:
            res.append(i)

    print(" ".join(res))
    
    


    
def check(l1, l2):
    if len(l1) != len(l2):
        return False
    else:
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False
    return True

n,m = map(int, input().split())
l1, l2 = [], []
line1 = list(map(int, input().split()))
for i in line1:
    if i not in l1:
        l1.append(i)
line2 = list(map(int , input().split()))
for i in line2:
    if i not in l2:
        l2.append(i)
l1.sort()
l2.sort()
print("YES" if check(l1, l2) else "NO")


















from datetime import datetime

class Phim:
    def __init__(self, ma, the_loai, ngay, thu_tu, so_tap):
        self.ma = ma
        self.the_loai = the_loai
        self.ngay = ngay
        self.thu_tu = thu_tu
        self.so_tap = so_tap
        self.ngay_obj = datetime.strptime(ngay, "%d/%m/%Y")
    def output(self):
        print(f"{self.ma} {self.the_loai} {self.ngay} {self.thu_tu} {self.so_tap}")
        
n,m = map(int, input().split())
l = []
cnt = 1
for _ in range(n):
    tloai = input().strip()
    l.append(tloai)
ans = []
for _ in range(m):
    ma_tl  = input().strip()
    char = int(ma_tl[2:]) - 1
    the_loai = l[char]
    ngay = input()
    thu_tu = input()
    so_tap = int(input())
    if (cnt <= 9):
        ma = "P00" + str(cnt)
    else:
        ma = "P0" + str(cnt)
    cnt += 1
    ans.append(Phim(ma, the_loai, ngay, thu_tu, so_tap))
ans.sort(key = lambda x : (x.ngay_obj, x.thu_tu, -x.so_tap))
for x in ans:
    x.output()








class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao
        
    def __add__(self, other):
        return SoPhuc(self.thuc + other.thuc, self.ao + other.ao)
    
    def __mul__(self, other):
        return SoPhuc(self.thuc * other.thuc- self.ao * other.ao, self.thuc * other.ao + self.ao * other.thuc)
    
    def __str__(self):
        if self.ao >= 0:
            return f"{self.thuc} + {self.ao}i"
        else:
            return f"{self.thuc} - {self.ao}i"
        
for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    A = SoPhuc(a,b)
    B = SoPhuc(c,d)
    tong = A + B
    C = tong * A
    D = tong * tong
    print(f"{C}, {D}")
 
 
 
 
 
 
 
 
 
 
 
 
 
        