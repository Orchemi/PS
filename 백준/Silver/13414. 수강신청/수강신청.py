import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
o1 = {}
o2 = {}
for i in range(1, M+1):
    log = sys.stdin.readline().rstrip()
    pre_order = o1.get(log, 0)
    o1[log] = i
    if pre_order:
        del o2[pre_order]
    o2[i] = log

for k in sorted(o2.keys())[:N]:
    print(o2[k])