import sys
input = sys.stdin.readline

N = int(input())
D = {}
for _ in range(N):
    n = int(input())
    D[n] = D.get(n, 0)+1

for k in sorted(D.keys()):
    for _ in range(D[k]):
        print(k)