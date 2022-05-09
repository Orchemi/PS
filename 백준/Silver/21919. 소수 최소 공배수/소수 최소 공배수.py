import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

M = max(arr)
v = [1]*(M+1)
v[0] = v[1] = 0
for i in range(2, M+1):
    if not v[i]: continue
    for j in range(i+i, M+1, i):
        v[j] = 0

ret = 1
for a in arr:
    if v[a]:
        ret *= a
        v[a] = 0

ans = -1 if ret == 1 else ret
print(ans)