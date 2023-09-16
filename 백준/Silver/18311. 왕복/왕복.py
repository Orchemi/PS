def main():
    N, K = map(int, input().split())
    parts = list(map(int, input().split()))
    if K == 0: return 1

    acc = 0
    for i in range(N):
        if acc > K:
            return i
        acc += parts[i]

    for i in range(N-1, 0, -1):
        acc += parts[i]
        if acc > K:
            return i+1
    return 1

print(main())