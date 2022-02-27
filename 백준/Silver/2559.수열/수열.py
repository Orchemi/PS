import sys; input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().split()))

sum_v = sum(arr[0:K])
max_v = sum_v
for i in range(N-K):
    sum_v += arr[K+i] - arr[i]
    if max_v < sum_v:
        max_v = sum_v

print(max_v)