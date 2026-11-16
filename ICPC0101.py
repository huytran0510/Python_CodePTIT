stack = []
n = int(input())
l = list(map(int, input().split()))
for i in l:
    if (len(stack) == 0):
        stack.append(i)
    else:
        x = stack[-1]
        if (i + x) % 2 == 0:
            stack.pop()
        else:
            stack.append(i)
print(len(stack))

