N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def f(i):
    if len(stack)==M:
        print(*stack)
        return

    check = 0
    for k in range(i, N):
        if check != nums[k]:
            check = nums[k]
            stack.append(nums[k])
            f(k)
            stack.pop()

stack = []
f(0)