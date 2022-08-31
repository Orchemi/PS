L = int(input())
arr = list(map(int, input().split()))
n = int(input())

maxx = max(arr)
S = set(arr)

cnt = 0
for s in range(1, maxx+1):
    if s > n: break
    if s in S: continue
    for e in range(s+1, maxx+1):
        if e in S: break
        if e < n: continue
        cnt += 1

print(cnt)