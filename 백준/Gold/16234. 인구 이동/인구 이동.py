import sys
input = sys.stdin.readline

def findUnion(i, j):
    global visited, N, L, R, POP
    visited[i][j] = 1
    unionQ = [(i, j)]
    start = -1
    end = 1

    while start < end-1:
        start += 1
        ni, nj = unionQ[start]
        didj = [(-1,0),(0,-1),(1,0),(0,1)]
        for di, dj in didj:
            if 0<=ni+di<N and 0<=nj+dj<N:
                if not visited[ni+di][nj+dj]:
                    if L <= abs(POP[ni][nj] - POP[ni+di][nj+dj]) <= R:
                        visited[ni+di][nj+dj] = 1
                        unionQ.append((ni+di, nj+dj))
                        end += 1
    return unionQ

N, L, R = map(int, input().split())
POP = [list(map(int, input().split())) for _ in range(N)]
ret = 0

while True:
    visited = [[0]*N for _ in range(N)]
    unions = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union = findUnion(i, j)
                if len(union) > 1:
                    unions.append(union)

    if not unions:
        break

    POP2 = []
    for lst in POP:
        POP2.append(lst[::])

    for union in unions:
        sum_pop = 0
        cnt = 0
        for country in union:
            ci, cj = country
            sum_pop += POP[ci][cj]
            cnt += 1

        avg_pop = sum_pop // cnt
        for country in union:
            ci, cj = country
            POP2[ci][cj] = avg_pop

    POP = POP2
    ret += 1

print(ret)