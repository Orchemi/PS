txt = input()
l = len(txt)
S = set()
for i1 in range(1, l-1):
    p1 = list(txt[:i1])[::-1]
    for i2 in range(i1+1, l):
        p2 = list(txt[i1:i2])[::-1]
        p3 = list(txt[i2:])[::-1]
        S.add(''.join((p1+p2+p3)))

print(sorted(list(S))[0])