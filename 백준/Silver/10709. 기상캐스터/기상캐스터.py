def main():
    def find_clouds():
        clouds = set()
        for i in range(I):
            for j in range(J):
                if mat[i][j] == 'c':
                    clouds.add((i, j))
        return clouds

    def move(v, i, j):
        if (i, j) in clouds or j==J: return
        ret[i][j] = v
        move(v+1, i, j+1)


    I, J = map(int, input().split())
    mat = [list(input()) for _ in range(I)]
    ret = [[-1]*J for _ in range(I)]
    clouds = find_clouds()
    for ci, cj in clouds:
        ret[ci][cj]=0
        move(1, ci, cj+1)

    for lst in ret:
        print(*lst)

main()