def check(n1, n2, l):
    p = 1
    while p<=l:
        if n1[:p]==n2[-p:]: return 1
        p += 1
    p = 1
    while p<=l:
        if n2[:p]==n1[-p:]: return 1
        p += 1
    return 0

N = int(input())
names = [input() for _ in range(N)]
ret = 0
for i in range(N-1):
    name1 = names[i]
    l1 = len(name1)
    for j in range(i+1, N):
        name2 = names[j]
        l2 = len(name2)
        ret += check(name1, name2, min(l1, l2))
print(ret)