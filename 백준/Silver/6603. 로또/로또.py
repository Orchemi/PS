def f(i, N, nums):
    if len(stack)==6:
        print(*stack)
        return

    for k in range(i, N):
        stack.append(nums[k])
        f(k+1, N, nums)
        stack.pop()

while True:
    all = input()
    if all=='0':
        break

    all = list(map(int, all.split()))
    k, *nums = all
    stack = []
    f(0, k, nums)
    stack = []
    print()