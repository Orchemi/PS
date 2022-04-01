import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def foo(s, e, d, cnt):
    if d == N:
        global maxCnt
        maxCnt = max(maxCnt, cnt)
        return

    if Ms[d][0] >= e:
        foo(Ms[d][0], Ms[d][1], d+1, cnt+1)
    else:
        foo(s, e, d+1, cnt)

N = int(input())
Ms = []
for _ in range(N):
    s, e = map(int, input().split())
    Ms.append((s, e))
Ms.sort(key=lambda x:(x[1], x[0]))
maxCnt = 0
foo(Ms[0][0], Ms[0][1], 1, 1)
print(maxCnt)