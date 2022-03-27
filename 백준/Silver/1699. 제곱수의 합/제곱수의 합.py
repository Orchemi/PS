from collections import deque

def BFS():
    N = int(input())
    me = [0]*(N+1)
    Q = deque()
    Q.append(0)

    v = 1
    while not me[N]:
        s = Q.popleft()
        k = 1
        while s+k**2 <= N and not me[N]:
            if not me[s+k**2]:
                Q.append(s+k**2)
                me[s+k**2] = me[s]+1
            k += 1
    print(me[N])

BFS()