def main():
    def select_boundary(i, j):
        area = []
        for si in range(i, i+W):
            for sj in range(j, j+W):
                area.append(mat[si][sj])
        return area


    I, J, K, W = map(int, input().split())
    ret = [[0]*(J-W+1) for _ in range(I-W+1)]
    m = (W**2)//2
    mat = [list(map(int, input().split())) for _ in range(I)]
    for i in range(I-W+1):
        for j in range(J-W+1):
            area = select_boundary(i, j)
            center = sorted(area)[m]
            ret[i][j] = center

    for l in ret:
        print(*l)

main()