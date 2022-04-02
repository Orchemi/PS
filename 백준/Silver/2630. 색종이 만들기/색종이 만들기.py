import sys
from collections import deque

def check(ni, nj, nl, nc):
    cnt = 0
    for i in range(ni, ni + nl):
        for j in range(nj, nj + nl):
            if not mat[i][j]==nc:
                return 0
    return 1


N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
cntW = cntB = 0
Q = deque()
Q.append((0,0,N))
while Q:
    ni, nj, nl = Q.popleft()
    nc = mat[ni][nj]
    if check(ni, nj, nl, nc):
        if nc:
            cntB += 1
        else:
            cntW += 1
    else:
        hl = nl//2
        Q.append((ni, nj, hl))
        Q.append((ni+hl, nj, hl))
        Q.append((ni, nj+hl, hl))
        Q.append((ni+hl, nj+hl, hl))

print(cntW)
print(cntB)