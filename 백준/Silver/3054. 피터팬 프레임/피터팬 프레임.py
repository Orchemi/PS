def draw(i, j, c):
    for k in (1, -1):
        for di, dj in ((2, 0), (1, 1), (0, 2), (1, -1)):
            si, sj = i+di*k, j+dj*k
            mat[si][sj] = c


txt = input()
L = len(txt)
mat = [['.']*(L*4+1) for _ in range(5)]
for i in range(L):
    mat[2][i*4+2] = txt[i]
    draw(2, i*4+2, '#')

for i in range(2, L, 3):
    draw(2, i*4+2, '*')

for l in mat:
    print(''.join(l))