def make_nums():
    nums = [1, 1]
    for _ in range(45):
        n = nums[-1]+nums[-2]
        nums.append(n)
    return nums

T = int(input())
nums = make_nums()
for _ in range(T):
    N = int(input())
    print(nums[N])