def main():
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    for _ in range(Q):
        inp = list(map(int, input().split()))
        if len(inp) == 1:
            A = [[0]*N for _ in range(N)]
            for i in range(1, N+1):
                for j in range(1, N+1):
                    A[j-1][N-i] = mat[i-1][j-1]
            mat = [lst[::] for lst in A]
        else:
            o, i = inp
            i -= 1
            mat[i] = [mat[i][N-1], *mat[i][:N-1]]

    return mat

mat = main()
for lst in mat:
    print(*lst)