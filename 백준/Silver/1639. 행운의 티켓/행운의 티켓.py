txt = input()
tl = len(txt)
maxx = 0
for sep in range(1, tl):
    n1, n2, cl = 0, 0, 0
    s, e = sep-1, sep
    while s>=0 and e<tl:
        n1 += int(txt[s])
        n2 += int(txt[e])
        cl += 2

        if n1==n2 and maxx < cl:
            maxx = cl

        s -= 1
        e += 1

print(maxx)