def main():
    N, M = map(int, input().split())
    A = {}
    for n in range(1, N+1):
        A[n] = set()
    for _ in range(M):
        a, b = map(int, input().split())
        A[a].add(b)
        A[b].add(a)

    cnt = 0
    for a in range(1, N+1):
        for b in range(a+1, N+1):
            if b in A[a]: continue
            for c in range(b+1, N+1):
                if c in A[a]: continue
                if c in A[b]: continue
                cnt += 1
    return cnt

print(main())