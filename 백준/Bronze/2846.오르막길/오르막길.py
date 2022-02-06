N = int(input())
nums = list(map(int, input().split()))
nums.append(0)

val_low = nums[0]
val_high = 0
val_max = 0

for i in range(1, N+1):
    if nums[i] > nums[i-1]:
        continue
    else:
        val_high = nums[i-1]

        if val_max < val_high-val_low:
            val_max = val_high-val_low

        val_low = nums[i]
        val_high = 0

print(val_max)