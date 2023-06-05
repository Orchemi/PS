import sys
sys.stdin.readline

def find_around(i, j):
    val = 0
    for si in range(i-1, i+2):
        if not (0<=si<N): continue
        for sj in range(j-1, j+2):
            if not (0<=sj<N): continue
            if mat[si][sj]=='.': continue
            val += int(mat[si][sj])
    return val if val < 10 else 'M'


N = int(input())
mat = [list(input()) for _ in range(N)]
ret = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if mat[i][j]=='.':
            ret[i][j] = find_around(i, j)
        else:
            ret[i][j] = '*'

for l in ret:
    print(*l, sep='')