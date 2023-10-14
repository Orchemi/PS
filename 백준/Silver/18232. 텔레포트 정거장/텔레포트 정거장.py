from collections import deque
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    S, E = map(int, input().split())
    A = [0]*300001
    A[S] = 1
    T = {}
    for _ in range(M):
        x, y = map(int, input().split())
        if not T.get(x, []): T[x] = []
        T[x].append(y)
        if not T.get(y, []): T[y] = []
        T[y].append(x)

    Q = deque([(S, 1)])
    while Q:
        n, cnt = Q.popleft()
        ts = T.get(n, [])
        for m in (n-1, n+1, *ts):
            if m == E: return cnt
            if not (0<=m<=300000): continue
            if A[m]: continue
            A[m] = cnt+1
            Q.append((m, cnt+1))

print(main())