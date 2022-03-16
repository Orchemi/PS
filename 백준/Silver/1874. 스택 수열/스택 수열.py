import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
k = 0
p = 1
ops = []
stack = []

while k < N:
    if not stack or nums[k] > stack[-1]:
        stack.append(p)
        ops.append('+')
        p += 1
        continue

    if stack[-1]==nums[k]:
        stack.pop()
        ops.append('-')
    k += 1

print('NO') if stack else print(*ops, sep='\n')