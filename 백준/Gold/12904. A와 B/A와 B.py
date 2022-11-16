from collections import deque

def main() :
    S = list(input())
    Q = deque(list(input()))
    D = {0:-1, -1:0}
    sl, ql = len(S), len(Q)
    i, op = 0, -1
    while i < ql-sl:
        i += 1
        p = Q.pop() if op else Q.popleft()
        if p == 'A': continue
        op = D[op]
        
    while Q:
        a = Q.pop() if op else Q.popleft()
        b = S.pop()
        if a!=b: return 0
    return 1

print(main())