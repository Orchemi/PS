N, M = map(int, input().split())
nums = list(map(int, input().split()))

max_v = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_v = nums[i] + nums[j] + nums[k]
            if sum_v <= M:
                if max_v < sum_v:
                    max_v = sum_v

print(max_v)