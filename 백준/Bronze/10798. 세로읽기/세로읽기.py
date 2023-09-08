mat = [list(input()) for _ in range(5)]
ls = [len(a) for a in mat]
ml = max(ls)

ret = ''
for j in range(ml):
    for i in range(5):
        if ls[i] <= j: continue
        ret += mat[i][j]

print(ret)