import sys
from collections import deque
input = sys.stdin.readline

def maxCheck():
    global Q
    max_imp = 0
    for order, imp in Q:
        if max_imp < imp:
            max_imp = imp
    return max_imp

T = int(input())
for _ in range(T):
    N, order = map(int, input().split())
    arr = list(map(int, input().split()))
    targetImps = arr[order]
    Q = deque()
    out = 0

    for idx, val in enumerate(arr):
        Q.append((idx, val))

    while True:
        mi = maxCheck()
        while True:
            no, ni = Q.popleft()
            if ni == mi:
                out += 1
                break
            else:
                Q.append((no, ni))

        if no==order:
            break

    print(out)