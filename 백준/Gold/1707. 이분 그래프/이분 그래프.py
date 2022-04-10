import sys
input = sys.stdin.readline
from collections import deque

def check():
    V, E = map(int, input().split())
    D = [2] * V
    G = [[] for _ in range(V)]
    for _ in range(E):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)

    for s in range(V):
        if D[s]==2:
            Q = deque()
            Q.append(s)
            D[s] = 0
            ql = 1

            cnt = 1
            while Q:
                for _ in range(ql):
                    u = Q.popleft()
                    ql -= 1
                    for v in G[u]:
                        # v 값이 초기값인 2일 때
                        if D[v]==2:
                            D[v] = cnt
                            Q.append(v)
                            ql += 1
                            continue

                        # D[v] 값이 cnt와 같다면 'False' return
                        if D[v]==cnt^1:
                            return 'NO'
                cnt ^= 1
    return 'YES'


T = int(input())
for _ in range(T):
    print(check())