from collections import deque

def main():
    S, T = map(int, input().split())
    Q = deque([(S, T, 0)])
    while Q:
        s, t, c = Q.popleft()
        if s==t: return c
        if s>t: continue
        Q.append((s*2, t+3, c+1))
        Q.append((s+1, t, c+1))

C = int(input())
for _ in range(C):
    print(main())