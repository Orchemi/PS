import sys
input = sys.stdin.readline
from collections import deque

V = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(V-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

Q = deque()
Q.append(1)
p = deque()
p.extend([0]*(V+1))
p[0] = p[1]= -1

while Q:
    k = Q.popleft()
    for h in tree[k]:
        if p[h]: continue
        p[h] = k
        Q.append(h)

p.popleft()
p.popleft()
while p:
    print(p.popleft())