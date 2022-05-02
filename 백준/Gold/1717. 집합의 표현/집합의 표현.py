import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def find_set(x):
    if x!=p[x]:
        p[x] = find_set(p[x])
    return p[x]


n, m = map(int, input().split())
p = [i for i in range(n+1)]
for _ in range(m):
    f, u, v = map(int, input().split())
    a, b = find_set(u), find_set(v)

    if f:
        print('YES' if a == b else 'NO')
        continue

    if a != b:
        p[a] = b