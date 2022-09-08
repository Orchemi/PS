def fill_order(n):
    global mat, N
    def check_like(n, i, j):
        global mat, N, likes_arr
        blank, ret = 0, 0
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            si, sj = i+di, j+dj
            if not (0<=si<N and 0<=sj<N): continue
            if not mat[si][sj]: blank += 1
            elif mat[si][sj] in likes_arr[n]: ret += 1
        return ret, blank

    ret = []
    max_like_cnt = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j]: continue
            check_like_ret, check_blank_ret = check_like(n, i, j)
            if max_like_cnt > check_like_ret: continue
            elif max_like_cnt == check_like_ret:
                ret.append((i, j, check_blank_ret))
            elif max_like_cnt < check_like_ret:
                max_like_cnt = check_like_ret
                ret = [(i, j, check_blank_ret)]
    return ret


N = int(input())
likes_arr = [set() for _ in range(N**2+1)]
orders = []
for _ in range(N**2):
    n, *likes = map(int, input().split())
    orders.append(n)
    likes_arr[n] = set(likes)

mat = [[0]*N for _ in range(N)]
for order in orders:
    points = fill_order(order)
    points.sort(key= lambda x: (-x[2], x[0], x[1]))
    ai, aj, ablank = points[0]
    mat[ai][aj] = order

def check_score(ki, kj):
    global mat, N, likes_arr
    n = mat[ki][kj]
    match = 0
    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        si, sj = i+di, j+dj
        if not (0<=si<N and 0<=sj<N): continue
        if not mat[si][sj]: continue
        if mat[si][sj] in likes_arr[n]: match += 1
    return 10**(match-1) if match else 0

scores = 0
for i in range(N):
    for j in range(N):
        scores += check_score(i, j)

print(scores)