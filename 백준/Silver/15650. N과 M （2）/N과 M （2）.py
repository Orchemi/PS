N, M = map(int, input().split())

def func(i, N, M):
    global stack
    global nolst
    if i==M+1:
        print(*stack)
        return

    start = stack[-1] if len(stack) else 1
    for k in range(start, N+1):
        if visited[k]:
            continue
        visited[k] = 1
        stack.append(k)
        func(i+1, N, M)
        visited[k] = 0
        stack.pop()

stack = []
nolst = []
visited = [0]*(N+1)
func(1, N, M)