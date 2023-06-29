N, C, T = map(int, input().split())
cnt = 0
while T:
    if T==1: break
    T = T//2
    cnt += 1

M = -1
while N:
    N //= 2
    M += 1

print(min(cnt+C, M))