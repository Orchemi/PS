def foo(ni, nj, nl):
    global ans

    nc = mat[ni][nj]
    for i in range(ni, ni+nl):
        for j in range(nj, nj+nl):
            if not mat[i][j] == nc:
                ans += '('
                hl = nl//2
                foo(ni, nj, hl)
                foo(ni, nj+hl, hl)
                foo(ni+hl, nj, hl)
                foo(ni+hl, nj+hl, hl)
                ans += ')'
                return
    ans += nc
    return

N = int(input())
mat = list(input() for _ in range(N))
ans = ''
foo(0, 0, N)
print(ans)