def bfs(N, K):
    global pos
    Q = [N]
    pos[N] = 0
    front = -1
    time = 1
    while pos[K] == -1:
        front += 1
        now = Q[front]
        if now > 0 and pos[now-1] == -1:
            pos[now-1] = pos[now]+1
            Q.append(now-1)
        if now < 10**5 and pos[now+1] == -1:
            pos[now+1] = pos[now]+1
            Q.append(now+1)
        if now <= 5*(10**4) and pos[now*2] == -1:
            pos[now*2] = pos[now]+1
            Q.append(now*2)
        time += 1
    return pos[K]

pos = [-1]*100001
N, K = map(int, input().split())

# 1. K가 N보다 작거나 같은 경우
if K <= N:
    print(N-K)
    quit()

# 2. K가 N보다 큰 경우
print(bfs(N, K))