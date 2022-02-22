n = int(input())
nums = list(map(int, input().split()))
max_val = min_val = nums[0]

for num in nums:

    if max_val < num:
        max_val = num
        continue

    elif min_val > num:
        min_val = num
        continue

    else:
        pass

print(min_val, max_val)