import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def main():
    def make_rels():
        rels = [[] for _ in range(N+1)]
        M = int(input())
        for _ in range(M):
            u, v, w = map(int, input().split())
            rels[u].append((v, w))
            rels[v].append((u, w))
        return rels

    def find_max_len():
        mi, mv = 0, 0
        Ds = [find_max_len_sub(f) for f in friends]
        for i in range(1, N+1):
            smv = 1e9
            for j in range(3):
                smv = min(smv, Ds[j][i])
            if Ds[j][i] == 1e9: continue
            if smv > mv:
                mi, mv = i, smv
        return mi


    def find_max_len_sub(n):
        visited = [0]*(N+1)
        D = [1e9 for _ in range(N+1)]
        D[n] = 0
        H = [(0, n)]
        while H:
            d, u = heappop(H)
            if visited[u]: continue
            visited[u] = 1
            for v, w in rels[u]:
                if visited[v]: continue
                if D[v] > D[u]+w:
                    D[v] = D[u]+w
                    heappush(H, (D[v], v))
        return D

    N = int(input())
    friends = set(map(int, input().split()))
    rels = make_rels()
    return find_max_len()

print(main())