import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
K = int(input())
arr = sorted(list(map(int, input().split())))

dp = [0]*N
for j in range(1, N):
    dp[j] = dp[j-1] + arr[j] - arr[j-1]
Q = deque()
Q.append(dp)

for i in range(1, K):
    Q.append([0]*N)
    for j in range(i+1, N):
        Q[1][j] = min(Q[1][j-1] + arr[j] - arr[j-1], Q[0][j-1])
    Q.popleft()

print(Q[0][-1])