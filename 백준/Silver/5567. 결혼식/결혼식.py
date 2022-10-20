N = int(input())
M = int(input())
arr = [set() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].add(b)
    arr[b].add(a)

S = arr[1]
for s in arr[1]:
    S = S | arr[s]

if 1 in S: S.remove(1)
print(len(S))