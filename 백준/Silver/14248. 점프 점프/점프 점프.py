import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = [0] + list(map(int, input().split()))
s = int(input())
cnt = 1
Q = deque([s])
S = set()
while Q:
    k = Q.popleft()
    step = arr[k]

    a = k-step
    if not a in S and a > 0:
        S.add(a)
        cnt += 1
        Q.append(a)

    b = k + step
    if not b in S and b <= N:
        S.add(b)
        cnt += 1
        Q.append(b)

print(cnt)