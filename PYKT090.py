with open ("CONTACT.in", "r") as f:
    mail = f.readlines()
s = set()
for x in mail:
    s.add(x.strip().lower())
for x in sorted(s):
    print(x)
