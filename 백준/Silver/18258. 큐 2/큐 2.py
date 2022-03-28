import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
Q = deque()
l = 0
for _ in range(N):
    a = input().split()
    f = a[0]
    if len(a) == 2:
        v = int(a[1])

    if f == 'push':
        Q.append(v)
        l += 1
    elif f == 'pop':
        if l:
            print(Q.popleft())
            l -= 1
        else:
            print(-1)
    elif f =='size':
        print(l)
    elif f == 'empty':
        print(1 if l==0 else 0)
    elif f == 'front':
        print(Q[0] if l else -1)
    elif f =='back':
        print(Q[-1] if l else -1)