from collections import deque

def main():
    def bfs(i, j):
        mat = [[0]*N for _ in range(N)]
        mat[i][j] = 1
        Q = deque([(i, j)])
        while Q:
            ni, nj = Q.popleft()
            for oi, oj in ((-1,2), (1,2), (2,1), (-2,1)):
                for o in ((-1, 1)):
                    di, dj = oi*o, oj*o
                    si, sj = ni+di, nj+dj
                    if not (0<=si<N and 0<=sj<N): continue
                    if mat[si][sj]: continue
                    Q.append((si, sj))
                    mat[si][sj]= mat[ni][nj]+1
        return mat

    N, M = map(int, input().split())
    i, j = map(lambda x: int(x)-1, input().split())
    mat = bfs(i, j)

    for _ in range(M):
        ki, kj = map(lambda x: int(x)-1, input().split())
        print(mat[ki][kj] - 1)

main()