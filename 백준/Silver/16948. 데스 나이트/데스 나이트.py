from collections import deque

def main():
    N = int(input())
    bi, bj, ti, tj = map(int, input().split())
    mat = [[0]*N for _ in range(N)]
    mat[bi][bj] = 1
    Q = deque([(bi, bj)])
    while Q:
        i, j = Q.popleft()
        for di, dj in ((-2,-1),(-2,1),(0,-2),(0,2),(2,-1),(2,1)):
            si, sj = i+di, j+dj
            if not (0<=si<N and 0<=sj<N): continue
            if si==ti and sj==tj: return mat[i][j]
            if mat[si][sj]: continue
            mat[si][sj] = mat[i][j]+1
            Q.append((si, sj))
    return -1

print(main())