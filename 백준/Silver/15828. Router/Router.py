import sys
input = sys.stdin.readline
from collections import deque

Q = deque()
l = 0
size = int(input())

while True:
    n = int(input())
    if n==-1: break
    if n==0:
        if not l: continue
        Q.popleft()
        l -= 1
    else:
        if l==size: continue
        Q.append(n)
        l += 1

print(*Q) if l else print('empty')