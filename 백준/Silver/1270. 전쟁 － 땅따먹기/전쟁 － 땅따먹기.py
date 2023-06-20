import sys
input = sys.stdin.readline

def main():
    N, *arr = map(int, input().split())
    type = set(arr)
    D = {}
    for t in type: D[t] = 0
    for a in arr: D[a] += 1
    for k, v in D.items():
        if v*2 > N: return k
    return 'SYJKGW'

T = int(input())
for _ in range(T):
    print(main())