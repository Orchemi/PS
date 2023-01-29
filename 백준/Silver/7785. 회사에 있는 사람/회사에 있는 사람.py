N = int(input())
S = set()
for _ in range(N):
    name, act = input().split()
    if name in S:
        S.remove(name)
    else:
        S.add(name)

for name in sorted(list(S), reverse=True):
    print(name)