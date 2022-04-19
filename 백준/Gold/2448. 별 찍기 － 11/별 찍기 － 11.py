def foo(ni, nj, M):
    if M == 3:
        k = 0
        while k < 3:
            for j in range(-k, k+1):
                mat[ni+k][nj+j] = '*'
            k += 1
        mat[ni+1][nj]=' '
        return

    H = M//2
    foo(ni, nj, H)
    foo(ni+H, nj-H, H)
    foo(ni+H, nj+H, H)


N = int(input())
mat = [[' ']*(2*N-1) for _ in range(N)]
foo(0, N-1, N)

for lst in mat:
    print(*lst, sep='')