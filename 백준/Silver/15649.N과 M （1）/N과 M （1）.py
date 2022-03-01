def func(i, N, M):
    global stack
    global visited

    if i == M+1:
        print(*stack)
        return

    for k in range(1, N+1):
        if not visited[k]:
            visited[k] = 1
            stack.append(k)
            func(i+1, N, M)
            visited[k] = 0
            stack.pop()
    return

N, M = map(int, input().split())
stack = []
visited = [0]*(N+1)

func(1, N, M)