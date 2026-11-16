t = int(input())
while t > 0:
    st = []
    s = input()
    cnt = 1
    for c in s:
        if c == '(':
            print(cnt,end= ' ')
            st.append(cnt)
            cnt += 1
        elif c == ')':
            print(st[-1], end = ' ')
            st.pop()
    print()
    t -= 1
