import sys
sys.setrecursionlimit(100000)

def foo(depth, floor, ceil, ssum):
    if depth==N:
        global maxV
        maxV = max(maxV, ssum)
        return

    maxNow = max(set(range(1, 7)) - {floor, ceil})
    floor = ceil
    ceil = cubes[depth+1][floor]
    foo(depth+1, floor, ceil, ssum+maxNow)


N = int(input())
cubes = []
for _ in range(N):
    a, b, c, d, e, f = map(int, input().split())
    dict1 = {a:f, b:d, c:e, d:b, e:c, f:a}
    cubes.append(dict1)
cubes.append(dict1)

maxV = 0
for i in range(1, 7):
    foo(0, i, cubes[0][i], 0)
print(maxV)
