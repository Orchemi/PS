def dfs(n, i, j):
    global sumV
    if n == 0:
        return
    if i==ti and j==tj:
        return
    si = 2**(n-1) if ti >= i+2**(n-1) else 0
    sj = 2**(n-1) if tj >= j+2**(n-1) else 0
    sumV += (si**2)*2+(sj**2)
    dfs(n-1, i+si, j+sj)

N, ti, tj = map(int, input().split())

sumV = 0
dfs(N, 0, 0)
print(sumV)