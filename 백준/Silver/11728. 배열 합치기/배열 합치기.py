import sys
input = sys.stdin.readline
from collections import deque

l1, l2 = map(int, input().split())
arr1 = deque(sorted(list(map(int, input().split()))))
arr2 = deque(sorted(list(map(int, input().split()))))
ret = []
while arr1 and arr2:
    if arr1[0] >= arr2[0]:
        ret.append(arr2.popleft())
    else:
        ret.append(arr1.popleft())

if arr1:
    ret.extend(arr1)
elif arr2:
    ret.extend(arr2)

print(*ret)