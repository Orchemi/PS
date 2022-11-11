def sub(c, t):
    for _ in range(t):
        print(c, end='')

def dfs(n, b):
    global N
    sub('*', n)
    sub(' ', b*2)
    sub('*', n)
    if n == N: return
    print()
    dfs(n+1, b-1)
    print()
    sub('*', n)
    sub(' ', b * 2)
    sub('*', n)

N = int(input())
dfs(1, N-1)