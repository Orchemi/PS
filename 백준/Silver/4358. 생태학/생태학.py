import sys

dic = dict()
cnt = 0
for a in sys.stdin:
    a = a.rstrip()
    dic[a] = dic.get(a, 0) + 1
    cnt += 1

for tree in sorted(dic.keys()):
    print(f'{tree} {dic[tree]*100/cnt:.4f}')