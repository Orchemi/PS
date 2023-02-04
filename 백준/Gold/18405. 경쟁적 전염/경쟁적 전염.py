def main():
    def find_position():
        P = [set() for _ in range(K+1)]
        for i in range(N):
            for j in range(N):
                P[mat[i][j]].add((i, j))

        mn, mx = 1, K
        while not P[mn]: mn += 1
        while not P[mx]: mx -= 1
        P[0] = set()
        return P, mn, mx


    def move():
        def move_one(i, j):
            v = mat[i][j]
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                si, sj = i+di, j+dj
                if not (0<=si<N and 0<=sj<N): continue
                if mat[si][sj]: continue
                mat[si][sj] = v
                add_set.add((si, sj))

        for v in range(mn, mx+1):
            if not P[v]: continue
            add_set = set()
            for i, j in P[v]:
                move_one(i, j)
            P[v] = add_set

    N, K = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    S, X, Y = map(int, input().split())
    P, mn, mx = find_position()

    for _ in range(S):
        move()
        while not P[mn] and mn < mx: mn+=1
        while not P[mx] and mn < mx: mx-=1
    return mat[X-1][Y-1]

print(main())