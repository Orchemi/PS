def func(i, N, M):
    global visited
    global stack

    if i == M:
        print(*stack)
        return

    if stack and stack_i[-1] == N-1:
        return

    start = stack_i[-1] if stack_i else 0
    for k in range(start, N):
        if not visited[k]:
            stack.append(nums[k])
            stack_i.append(k)
            visited[k] = 1

            func(i+1, N, M)

            stack.pop()
            stack_i.pop()
            visited[k] = 0


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

stack = []
stack_i = []
visited=[0]*(nums[-1]+1)
func(0, N, M)