from collections import deque

def BFS(v):
    Q = deque()
    Q.append((0, 0, 0))
    visit[0][0][0] = 1
    ql = 1
    cnt = 1
    while Q:
        for _ in range(ql):
            ni, nj, bw = Q.popleft()
            ql -= 1
            if ni==I-1 and nj==J-1: return cnt

            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                si, sj = ni+di, nj+dj
                if not (0<=si<I and 0<=sj<J): continue
                sw = bw + mat[si][sj]
                if sw > 1: continue
                if visit[si][sj][sw]: continue
                visit[si][sj][sw] = 1
                Q.append((si, sj, sw))
                ql += 1
        cnt += 1

    return -1

I, J = map(int, input().split())
mat = [list(map(int, input())) for _ in range(I)]
visit = [[[0]*3 for _ in range(J)] for _ in range(I)]

print(BFS(mat))