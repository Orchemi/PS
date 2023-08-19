def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    maxx = curr = 0
    s = 0

    for e in range(N):
        curr += A[e]

        while curr > M:
            curr -= A[s]
            s += 1

        maxx = max(maxx, curr)

    return maxx

print(main())