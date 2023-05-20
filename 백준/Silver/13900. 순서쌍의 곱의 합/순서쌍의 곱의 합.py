from collections import deque

N = int(input())
arr = list(map(int, input().split()))
acc = deque([arr[-1]])
for i in range(N-2, 0, -1):
    acc.appendleft(acc[0]+arr[i])

ret = 0
for i in range(N-1):
    ret += acc[i]*arr[i]
print(ret)