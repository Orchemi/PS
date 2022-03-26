def f(i, j, txt):
    if len(txt)==6:
        global arrSet
        arrSet.add(txt)
        return

    didj = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for di, dj in didj:
        si, sj = i+di, j+dj
        if not (0<=si<5 and 0<=sj<5): continue
        f(si, sj, txt+mat[si][sj])

mat = [list(input().split()) for _ in range(5)]
arrSet = set()
for i in range(5):
    for j in range(5):
        f(i, j, mat[i][j])

print(len(arrSet))