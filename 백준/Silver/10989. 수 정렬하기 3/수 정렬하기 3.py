import sys
input = sys.stdin.readline

dictA = {}
N = int(input())
for _ in range(N):
    a = int(input())
    dictA[a] = dictA.get(a, 0) + 1

max_v = max(list(dictA.keys()))
for i in range(1, max_v+1):
    k = dictA.get(i, 0)
    for _ in range(k):
        print(i)