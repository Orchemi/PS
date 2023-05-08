txt = input()
l = len(txt)
arr = []
for i1 in range(1, l-1):
    part1 = txt[:i1]
    rev1 = part1[::-1]

    for i2 in range(i1+1, l):
        part2 = txt[i1:i2]
        part3 = txt[i2:]
        rev2, rev3 = part2[::-1], part3[::-1]

        ret = rev1+rev2+rev3
        arr.append(ret)

print(sorted(arr)[0])