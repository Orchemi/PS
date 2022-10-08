import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    L = 2*K+1
    D = {}
    arr = []
    for _ in range(N):
        v, k = map(int, input().split())
        D[k] = v
        arr.append(k)
    arr.sort()

    si = ei = 0
    maxx = now = 0
    while ei < N:
        if arr[ei] > arr[si]+L:
            ei -= 1
            maxx = now
            break
        now += D[arr[ei]]
        ei += 1

    if ei == N:
        return now

    ei += 1

    while ei < N:
        now += D[arr[ei]]
        while arr[ei]-L > arr[si]:
            now -= D[arr[si]]
            si += 1
        if maxx < now:
            maxx = now

        ei += 1

    return maxx

print(main())