def main():
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    std = (N * (N**2+1))//2

    S = set()
    for i in range(N):
        for j in range(N):
            if mat[i][j] in S: return 'FALSE'
            S.add(mat[i][j])

    for lst in mat:
        if sum(lst) != std: return 'FALSE'

    for j in range(N):
        lst = [mat[i][j] for i in range(N)]
        if sum(lst) != std: return 'FALSE'

    lst = [mat[i][i] for i in range(N)]
    if sum(lst) != std: return 'FALSE'

    lst = [mat[i][N-1-i] for i in range(N)]
    if sum(lst) != std: return 'FALSE'
    return 'TRUE'

print(main())