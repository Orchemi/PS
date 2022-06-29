import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
acc = [0]
for i in range(N):
    acc.append(acc[-1]+arr[i])

cnt = 0
s = e = 0
while s<=e<=N:
    diff = acc[e] - acc[s]
    if diff > M:
        s += 1
    elif diff < M:
        e += 1
    else:
        cnt += 1
        s += 1
        e += 1

print(cnt)