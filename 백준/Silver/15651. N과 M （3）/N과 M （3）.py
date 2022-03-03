def func(i, N, M):
    global stack
    if i==M:
        print(*stack)
        return

    for k in range(1,N+1):
        stack.append(k)
        func(i+1, N, M)
        stack.pop()


N, M = map(int, input().split())
stack = []
func(0, N, M)