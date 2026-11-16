n = int(input())
l = []
for i in range(n):
    x = int(input())
    l.append(x)
l.sort(reverse= True)
print(f"Silver = {l[1]}")