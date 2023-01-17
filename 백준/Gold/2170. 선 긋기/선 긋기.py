import sys
input = sys.stdin.readline

N = int(input())
d = {}
for _ in range(N):
    s, e = map(int, input().split())
    v = d.get(s, 1e10)
    if v == 1e10 or v < e:
        d[s] = e

arr = sorted([(k, v) for k, v in d.items()])
ret = 0
tmps, tmpe = arr[0]

for s, e in arr[1:]:
    if tmpe < s:
        ret += tmpe - tmps
        tmps, tmpe = s, e
        continue

    tmpe = max(tmpe, e)

ret += tmpe - tmps
print(ret)