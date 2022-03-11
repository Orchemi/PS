N = int(input())
mat = [list(map(int, input())) for _ in range(N)]

def bfs(ni, nj):
    global N
    global Q
    global mat

    if not (0<=ni<N and 0<=nj<N):
        return 0

    if not mat[ni][nj]:
        return 0

    mat[ni][nj] = 0
    return 1 + bfs(ni, nj+1) + bfs(ni, nj-1) + bfs(ni-1, nj) + bfs(ni+1, nj)

Q = []

ret = []
for i in range(N):
    for j in range(N):
        if mat[i][j]:
            ret.append(bfs(i, j))

ret.sort()
print(len(ret))
for i in ret:
    print(i)