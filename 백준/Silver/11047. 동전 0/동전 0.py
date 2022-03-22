N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.reverse()

cnt = 0
for i in range(N):
    if not K: break
    if not K//arr[i]: continue
    cnt += K // arr[i]
    K %= arr[i]

print(cnt)