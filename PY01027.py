def check(s):
    for c in s:
        if c != '6' and c != '8':
            return 'NO'
    if s[0] == '8':
        return 'NO'
    if '888' in s:
        return 'NO'
    return 'YES'
s = input()
print(check(s))