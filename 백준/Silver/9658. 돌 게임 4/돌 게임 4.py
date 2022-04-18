import sys
input = sys.stdin.readline

N = int(input())
X = 10 if N<6 else N
arr = [0]*(X+1)
arr[1] = arr[3] = 1

k = 5
while k <= N:
    f = 0
    for i in (1, 3, 4):
        if arr[k-i]:
            f = 1
            break
    if not f:
        arr[k] = 1
    k += 1

print('CY' if arr[N] else 'SK')