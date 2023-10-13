from collections import deque

def main():
    A, B, N, M = map(int, input().split())
    if N==M: return 0
    arr = [0]*100001
    Q = deque([(N, 1)])
    while Q:
        n, cnt = Q.popleft()
        for m in (n-1, n+1, n-A, n+A, n-B, n+B, n*A, n*B):
            if not (0<=m<=100000): continue
            if arr[m]: continue
            if m==M: return cnt
            arr[m] = cnt+1
            Q.append((m, cnt+1))

print(main())