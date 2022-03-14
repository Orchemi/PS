import sys
input = sys.stdin.readline

N = int(input())
nums = sorted([int(input()) for _ in range(N)])
for i in range(N):
    print(nums[i])