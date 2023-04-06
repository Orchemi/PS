from collections import deque

def main():
    I, J = 10, 9
    bi, bj = map(int, input().split())
    ti, tj = map(int, input().split())
    D = {
        (-1,0): [(-1,-1),(-1,1)],
        (1,0): [(1,1),(1,-1)],
        (0,1): [(-1,1),(1,1)],
        (0,-1): [(-1,-1),(1,-1)]
    }

    Q = deque([(bi, bj)])
    visit = [[0]*J for _ in range(I)]
    visit[bi][bj] = 1

    while Q:
        ni, nj = Q.popleft()
        for i1, j1 in D.keys():
            si1, sj1 = ni+i1, nj+j1
            if not (0<=si1<I and 0<=sj1<J): continue
            if si1==ti and sj1==tj: continue
            for i2, j2 in D[(i1, j1)]:
                si2, sj2 = si1+i2, sj1+j2
                if si2==ti and sj2==tj: continue
                si3, sj3 = si2+i2, sj2+j2
                if not (0<=si3<I and 0<=sj3<J): continue
                if visit[si3][sj3]: continue
                if si3==ti and sj3==tj: return visit[ni][nj]
                visit[si3][sj3] = visit[ni][nj]+1
                Q.append((si3, sj3))

    return -1

print(main())