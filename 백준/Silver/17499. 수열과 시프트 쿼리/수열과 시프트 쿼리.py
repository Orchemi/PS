import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
arr = list(map(int, input().split()))
h = 0
for _ in range(Q):
    o = list(map(int, input().split()))
    if o[0] == 1:
        arr[(h + o[1] - 1) % N] += o[2]
    elif o[0] == 2:
        h = (h - o[1]) % N
    else:
        h = (h + o[1]) % N

print(*arr[h:], *arr[:h])