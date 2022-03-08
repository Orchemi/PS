def f(i, N, M):
    if i == M:
        print(*stack)
        return

    start = stack_k[-1] if stack_k else 0
    for k in range(start, N):
        stack_k.append(k)
        stack.append(nums[k])
        f(i+1, N, M)
        stack_k.pop()
        stack.pop()

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
stack_k = []
stack = []
f(0, N, M)