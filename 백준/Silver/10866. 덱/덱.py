import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
DQ = deque()
size = 0
for _ in range(N):
    a = input().split()
    if len(a)==2:
        pushN = a[1]
    Fn = a[0]

    if Fn == 'push_front':
        DQ.appendleft(pushN)
        size += 1

    elif Fn == 'push_back':
        DQ.append(pushN)
        size += 1

    elif Fn == 'pop_front':
        print(DQ.popleft() if size else -1)
        size = size-1 if size else 0

    elif Fn == 'pop_back':
        print(DQ.pop() if size else -1)
        size = size-1 if size else 0

    elif Fn == 'size':
        print(size)

    elif Fn == 'empty':
        print(0 if size else 1)

    elif Fn == 'front':
        print(DQ[0] if size else -1)

    elif Fn == 'back':
        print(DQ[-1] if size else -1)