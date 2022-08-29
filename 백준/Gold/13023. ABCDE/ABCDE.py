import sys
input = sys.stdin.readline


def dfs(u, i):
    global stack, arr
    if i == 5: return True
    for v in arr[u]:
        if v in stack: continue
        stack.append(v)
        if dfs(v, i+1): return True
        stack.pop()
    return False

N, M = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

stack = []
ans = 0
for i in range(N):
    if dfs(i, 0):
        ans = 1
        break

print(ans)