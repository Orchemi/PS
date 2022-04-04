import sys
input = sys.stdin.readline

def ssum(n):
    global arr2, last
    if n < 0:
        return 0

    while not arr2[n]:
        last += 1
        arr2[last] = arr2[last-1] + arr[last]
    return arr2[n]

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = [0]*100001
last = 0
arr2[0] = arr[0]

for _ in range(M):
    s, e = map(int, input().split())
    print(ssum(e-1)-ssum(s-2))