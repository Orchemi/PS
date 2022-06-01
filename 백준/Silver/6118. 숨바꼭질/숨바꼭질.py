import sys
input = sys.stdin.readline
from collections import deque

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
visit = [0]*(V+1)
for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

# 1부터 deque에 넣고 탐색 시작
Q = deque()
Q.append(1)
visit[1] = 1
n = 1

dis = 0
while n < V and Q:
    same_dis = []
    for _ in range(len(Q)):
        s = Q.popleft()
        # if visit[s]: continue
        # n += 1

        for e in G[s]:
            if visit[e]: continue
            Q.append(e)
            visit[e] = 1
            n += 1
            same_dis.append(e)

    dis += 1
    # print(dis)
    # print(same_dis)
    # print(visit)

# print(dis)
# print(same_dis)
print(min(same_dis), dis, len(same_dis))