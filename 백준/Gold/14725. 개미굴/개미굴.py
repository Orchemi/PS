import sys
input = sys.stdin.readline
from collections import deque

def main(position, Q):
    if not Q: return
    front = Q.popleft()
    root = position.get(front, dict())
    if not root:
        position[front] = dict()
    main(position[front], Q)

def check(position, depth):
    for k in sorted(position.keys()):
        print(f"{'--'*depth}{k}")
        if position[k]:
            check(position[k], depth+1)

GMG = dict()
T = int(input())
for _ in range(T):
    N, *roots = input().split()
    main(GMG, deque(roots))
check(GMG, 0)