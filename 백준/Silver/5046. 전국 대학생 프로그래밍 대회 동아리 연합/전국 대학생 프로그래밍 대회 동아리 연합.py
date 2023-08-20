def main():
    N, M, H, W = map(int, input().split())
    minn = 1e6
    for _ in range(H):
        B = int(input())
        weeks = list(map(int, input().split()))

        if N*B > M: continue
        if max(weeks) < N: continue
        minn = min(minn, N*B)
    return 'stay home' if minn == 1e6 else minn

print(main())