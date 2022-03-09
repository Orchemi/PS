N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def f():
    if len(stack)==M:
        print(*stack)
        return

    check = 0
    start = stack_k[-1] if stack_k else 0
    for k in range(start, N):
        if not visited[k] and check != nums[k]:
            check = nums[k]
            stack_k.append(k)
            visited[k] = 1
            stack.append(nums[k])
            f()
            stack_k.pop()
            visited[k] = 0
            stack.pop()

visited=[0]*N
stack = []
stack_k = []
f()