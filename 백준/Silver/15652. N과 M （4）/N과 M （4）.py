def func(i, N, M):
    if i==M:
        print(*stack)
        return

    start = stack[-1] if stack else 1
    for k in range(start, N+1):
        stack.append(k)
        func(i+1, N, M)
        stack.pop()

stack = []
N, M = map(int, input().split())
func(0, N, M)