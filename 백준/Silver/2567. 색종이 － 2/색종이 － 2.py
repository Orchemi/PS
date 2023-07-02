def main():
    def bfs(pi, pj):
        cnt = 0
        S = set()
        S.add((pi, pj))
        while S:
            i, j = S.pop()
            if visited[i][j]: continue
            visited[i][j] = 1
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                si, sj = i+di, j+dj
                if not (0<=si<101 and 0<=sj<101): continue
                if mat[si][sj]:
                    if visited[si][sj]: continue
                    S.add((si, sj))
                else:
                    cnt += 1
        return cnt


    N = int(input())
    mat = [[0]*101 for _ in range(101)]
    visited = [[0]*101 for _ in range(101)]
    pos = set()

    for _ in range(N):
        i, j = map(int, input().split())
        pos.add((i, j))
        for si in range(i, i+10):
            for sj in range(j, j+10):
                mat[si][sj] = 1

    cnt = 0
    for pi, pj in pos:
        if visited[pi][pj]: continue
        cnt += bfs(pi, pj)
    return cnt

print(main())