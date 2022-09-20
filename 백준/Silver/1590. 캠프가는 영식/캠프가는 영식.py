import sys
input = sys.stdin.readline

N, T = map(int, input().split())
minn = 2e6
for _ in range(N):
    S, I, C = map(int, input().split())
    if S+(I*(C-1)) < T: continue
    while C:
        if S >= T:
            if minn > S-T:
                minn = S-T
            break
        S += I
        C -= 1
print(-1 if minn == 2e6 else minn)