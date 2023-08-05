from collections import deque

def main():
    Q = deque()
    A, K = map(int, input().split())
    Q.append((0, A))
    visited = {A: 0}

    while Q:
        cnt, v = Q.popleft()
        for nv in (v*2, v+1):
            if nv == K: return cnt+1
            if nv > K: continue
            if nv in visited: continue
            visited[nv] = cnt+1
            Q.append((cnt+1, nv))

print(main())