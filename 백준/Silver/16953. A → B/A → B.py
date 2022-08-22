from collections import deque

def main():
    a, b = map(int, input().split())
    Q = deque()
    Q.append((a, 0))


    while Q:
        k, cnt = Q.popleft()
        if k == b: return cnt+1
        if k > b: continue
        Q.append((int(str(k)+'1'), cnt+1))
        Q.append((k*2, cnt+1))
    return -1

print(main())