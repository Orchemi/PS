def main():
    def move():
        d, s = map(int, input().split())
        di, dj = DD[d]
        for i in range(len(clouds)):
            ci, cj = clouds[i]
            si = check_over(ci+di*s)
            sj = check_over(cj+dj*s)
            clouds[i] = (si, sj)

    def check_over(n):
        while n < 0: n += N
        while n >= N: n -= N
        return n

    def rain():
        for ci, cj in clouds:
            mat[ci][cj] += 1

    def copy_water():
        for ci, cj in clouds:
            cnt_around = count_around(ci, cj)
            mat[ci][cj] += cnt_around

    def count_around(i, j):
        cnt_around = 0
        for di, dj in ((-1,-1),(-1,1),(1,-1),(1,1)):
            si, sj = i+di, j+dj
            if not (0<=si<N and 0<=sj<N): continue
            if not mat[si][sj]: continue
            cnt_around += 1
        return cnt_around

    def count_mat():
        cnt = 0
        for i in range(N):
            for j in range(N):
                cnt += mat[i][j]
        return cnt

    def make_cloud(clouds):
        new_clouds = []
        clouds_set = set(clouds)
        for i in range(N):
            for j in range(N):
                if (i, j) in clouds_set: continue
                if mat[i][j] < 2: continue
                mat[i][j] -= 2
                new_clouds.append((i, j))
        return new_clouds

    N, M = map(int, input().split())
    DD = [(0,0),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
    mat = [list(map(int, input().split())) for _ in range(N)]
    clouds = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]
    for _ in range(M):
        move()
        rain()
        copy_water()
        clouds = make_cloud(clouds)
    return count_mat()

print(main())