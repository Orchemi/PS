N = int(input())
S = {int(input()) for _ in range(N)}
ret = 4
for s in S:
    for k in range(5):
        r = {n for n in range(s-4+k, s+1+k)}
        if -1 in r: continue
        ret = min(ret, len(r-S))
print(ret)