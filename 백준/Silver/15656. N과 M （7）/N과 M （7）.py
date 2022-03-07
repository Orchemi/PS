def f(i, N, M):
    global stack

    if i == M:
        print(*stack)
        return

    for k in range(N):
        stack.append(nums[k])
        f(i+1, N, M)
        stack.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

stack = []
f(0, N, M)