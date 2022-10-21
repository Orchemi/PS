def check(i, j):
    global mat, remove_lst, I, J
    cnt = 0
    for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
        si, sj = i+di, j+dj
        if not (0<=si<I and 0<=sj<J): continue
        if mat[si][sj] == 'X': cnt += 1

    if cnt < 2:
        remove_lst.append((i, j))


I, J = map(int, input().split())
mat = [list(input()) for _ in range(I)]
remove_lst = []
for i in range(I):
    for j in range(J):
        if not mat[i][j]=='X': continue
        check(i, j)

for i, j in remove_lst:
    mat[i][j] = '.'


for i in range(I):
    for j in range(J):
        if mat[i][j]=='X':
            mxi = i
            break


for i in range(I-1, -1, -1):
    for j in range(J):
        if mat[i][j]=='X':
            mni = i
            break

for j in range(J):
    for i in range(I):
        if mat[i][j] == 'X':
            mxj = j
            break

for j in range(J-1, -1, -1):
    for i in range(I):
        if mat[i][j] == 'X':
            mnj = j
            break

for i in range(mni, mxi+1):
    for j in range(mnj, mxj+1):
        print(mat[i][j], end='')
    print()