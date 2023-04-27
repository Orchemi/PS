import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(input().split())
lions = []
for i in range(N):
    if arr[i]=='1':
        lions.append(i)

ret = 1e6
for i in range(len(lions)-K+1):
    ret = min(ret, lions[i+K-1]-lions[i]+1)
print(-1 if ret==1e6 else ret)