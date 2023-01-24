M = int(input())
cur = 1
for _ in range(M):
    S = set(map(int, input().split()))
    if not cur in S: continue
    S.remove(cur)
    cur = S.pop()

print(cur)