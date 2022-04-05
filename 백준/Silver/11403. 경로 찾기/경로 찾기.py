import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque

def run(i, s):
    global Q, check

    for v in link[s]:
        if check[i][v]: continue
        check[i][v] = 1
        run(i, v)
    return

N = int(input())
link = [[] for _ in range(N)]
check = [[0]*N for _ in range(N)]
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(N):
        if lst[j]:
            link[i].append(j)

for i in range(N):
    Q = deque()
    Q.extend(link[i])
    run(i, i)


for l in check:
    print(*l)