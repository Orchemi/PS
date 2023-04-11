X = int(input())
cnt = 0
T = 2
while T < X:
    N = 1
    while X-N-T >= N+2:
        cnt += 1
        N += 1
    T += 2
print(cnt)