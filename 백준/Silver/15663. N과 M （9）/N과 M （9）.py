N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [0]*N
stack = []

def f():
    if len(stack) == M:
        print(*stack)
        return

    check = 0
    for k in range(N):
        if not visited[k] and check != nums[k]:
            visited[k] = 1
            stack.append(nums[k])
            check = nums[k]
            f()
            visited[k] = 0
            stack.pop()

f()