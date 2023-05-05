from collections import deque

N = int(input())
Q = deque([i for i in range(1, N+1)])

while Q:
    c = Q.popleft()
    print(c, end=' ')

    if not Q: break
    c = Q.popleft()
    Q.append(c)