def replace(k):
    global N
    if k < 0:
        while k < 0:
            k += N
    if k >= N:
        while k >= N:
            k -= N
    return k

def move():
    global N, mat, tog, t, direction
    for i in range(N):
        for j in range(N):
            while mat[i][j][t]:
                m, d, s = mat[i][j][t].pop()
                di, dj = direction[d]
                si, sj = replace(i+di*s), replace(j+dj*s)
                if not (0<=si<N and 0<=sj<N): continue
                mat[si][sj][tog[t]].append([m, d, s])
    t^=1


def union_and_divide():
    global N, mat, t, direction
    multi_fireball = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dir = 1
            fireball_cnt = len(mat[i][j][t])
            if fireball_cnt > 1:
                multi_fireball[i][j] = 1
            while mat[i][j][t]:
                m, d, s = mat[i][j][t].pop()
                if not mat[i][j][t]: break
                std_dir = mat[i][j][t][0][1]
                if std_dir%2 != d%2: dir = 0
                mat[i][j][t][0][0] += m
                mat[i][j][t][0][2] += s

            if not fireball_cnt: continue
            if multi_fireball[i][j]:
                new_m = m//5
                if new_m:
                    new_s = s//fireball_cnt
                    for k in range(1-dir, 8, 2):
                        mat[i][j][tog[t]].append([new_m, k, new_s])
            else:
                mat[i][j][tog[t]].append([m, d, s])
    t^=1

# def SM(mat):
#     for l in mat:
#         print(*l)
#     print()


direction = {
    0: (-1, 0),
    1: (-1, 1),
    2: (0, 1),
    3: (1, 1),
    4: (1, 0),
    5: (1, -1),
    6: (0, -1),
    7: (-1, -1)
}

t = 0
tog = {1:0, 0:1}
N, M, K = map(int, input().split())
mat = [[[[], []] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, mass, speed, direc = map(int, input().split())
    mat[r-1][c-1][t].append([mass, direc, speed])

for _ in range(K):
    move()
    union_and_divide()

# 카운트
ret = 0
for i in range(N):
    for j in range(N):
        while mat[i][j][0]:
            m, d, s = mat[i][j][0].pop()
            ret += m

print(ret)