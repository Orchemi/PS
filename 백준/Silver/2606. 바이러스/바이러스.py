import sys; input = sys.stdin.readline

N = int(input())
E = int(input())

lst = [[] for _ in range(N+1)]
for _ in range(E):
    n, m = map(int, input().split())
    lst[n].append(m)
    lst[m].append(n)

def dfs(i):
    global cnt

    ls = lst[i]
    for v in ls:
        if not visited[v]:
            cnt += 1
            visited[v]=1
            dfs(v)

visited = [0] * (N+1)
cnt = 0
dfs(1)

print(cnt-1)