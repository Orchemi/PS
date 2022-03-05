def func(i, M):
    global nums
    global stack

    if i == M:
        print(*stack)
        return

    for k in nums:
        if visited[k]:
            visited[k] = 0
            stack.append(k)
            func(i+1, M)
            stack.pop()
            visited[k] = 1

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [1]*(nums[-1]+1)
stack = []

func(0, M)