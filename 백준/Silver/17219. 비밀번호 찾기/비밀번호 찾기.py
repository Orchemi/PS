dictA = {}
N, M = map(int, input().split())
for _ in range(N):
    s, p = input().split()
    dictA[s] = p

for _ in range(M):
    print(dictA[input()])