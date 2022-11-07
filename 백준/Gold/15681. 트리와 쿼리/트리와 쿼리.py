import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def calc_subtree(u):
    global visit, rels, S
    if visit[u]: return 0
    visit[u] = 1

    cnt = 1
    for v in rels[u]:
        if visit[v]: continue
        cnt += calc_subtree(v)

    S[u] = cnt
    return cnt


V, R, Q = map(int, input().split())
rels = [[] for _ in range(V+1)]
visit = [0]*(V+1)
S = [0]*(V+1)

for _ in range(V-1):
    u, v = map(int, input().split())
    rels[u].append(v)
    rels[v].append(u)

calc_subtree(R)
for _ in range(Q):
    print(S[int(input())])