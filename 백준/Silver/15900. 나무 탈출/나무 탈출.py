import sys
input = sys.stdin.readline
sys.setrecursionlimit(500000)

def find_child(p, c, d):
    global rel, ssum
    rel[c].remove(p)
    if not rel[c]:
        ssum += d
        return

    for nc in rel[c]:
        find_child(c, nc, d+1)


N = int(input())
rel = [set() for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    rel[a].add(b)
    rel[b].add(a)

ssum = 0
for c in rel[1]:
    find_child(1, c, 1)
print('Yes' if ssum%2 else 'No')