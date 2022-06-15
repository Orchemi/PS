import sys
input = sys.stdin.readline

def check(N):
    global arr
    cnt = 0
    l = r = N
    while not arr[l]:
        cnt += 1
        l -= 1

    while not arr[r]:
        cnt += 1
        r += 1

    return cnt

N = int(input())
inputs = [int(input()) for _ in range(N)]
M = 1299710
arr = [1]*M
arr[0] = arr[1] = 0
for a in range(2, M):
    if arr[a]:
        for b in range(a+a, M, a):
            arr[b] = 0

for n in inputs:
    print(check(n))