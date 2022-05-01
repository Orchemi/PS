import sys
input = sys.stdin.readline

def dfs(i):
    global order, visit, nzeros

    if i == nzl:
        check()
        return

    for k in range(i, nzl):
        nzeros[i], nzeros[k] = nzeros[k], nzeros[i]
        dfs(i+1)
        nzeros[i], nzeros[k] = nzeros[k], nzeros[i]


def check():
    global minCost
    costs = potions[::]
    nowCost = 0

    i = 0
    while i < nzl:
        buy = nzeros[i]
        nowCost += costs[buy]
        for fi, fc in dcs[buy]:
            costs[fi] = costs[fi]-fc if costs[fi]-fc > 0 else 1
        i += 1

    for i in zeros:
        nowCost += costs[i]

    minCost = min(minCost, nowCost)


pl = int(input())
potions = [0] + list(map(int, input().split()))

dcs = [[] for _ in range(pl+1)]

zl = nzl = 0
zeros = []
nzeros = []

for i in range(1, pl+1):
    dl = int(input())
    if not dl:
        zl += 1
        zeros.append(i)
        continue

    nzl += 1
    nzeros.append(i)
    for _ in range(dl):
        fi, fc = map(int, input().split())
        dcs[i].append((fi, fc))

minCost = 0xffffff
dfs(0)
print(minCost)