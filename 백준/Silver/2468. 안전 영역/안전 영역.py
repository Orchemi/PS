import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def check(i, j):
    global v, vstack
    for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
        si, sj = i+di, j+dj
        if not (0<=si<N and 0<=sj<N): continue
        if v[si][sj]: continue
        v[si][sj] = 1
        vstack.append((si, sj))
        check(si, sj)
    return


N = int(input())
high = [[] for _ in range(101)]
mat = []
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(N):
        high[lst[j]].append((i, j))
    mat.append(lst)

v = [[0]*N for _ in range(N)]
vstack = []
maxCnt = 1
h = 0
while h<101:
    cnt = 0
    if not high[h]:
        h += 1
        continue
    for i, j in high[h]:
        v[i][j] = 1

    for i in range(N):
        for j in range(N):
            if not v[i][j]:
                check(i, j)
                cnt += 1

    while vstack:
        vi, vj = vstack.pop()
        v[vi][vj] = 0

    maxCnt = max(maxCnt, cnt)
    h += 1
print(maxCnt)