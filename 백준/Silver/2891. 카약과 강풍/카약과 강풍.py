cnt = 0
N, S, R = map(int, input().split())
Bs = set(map(int, input().split()))
As = set(map(int, input().split()))
Cs = sorted(list(Bs-As))
FAs = As-Bs
for c in Cs:
    if c-1 in FAs:
        FAs.remove(c-1)
        continue

    if c+1 in FAs:
        FAs.remove(c+1)
        continue

    cnt += 1

print(cnt)