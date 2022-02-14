nums = input()

nums_ls_s = nums.split(' ')
nums_ls_d = [int(i) for i in nums_ls_s]

print(sum(nums_ls_d))