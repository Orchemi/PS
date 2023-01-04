def main():
    N, M = map(int, input().split())
    cnt, n = 0, 1
    while N >= n:
        if N%n:
            n += 1
            continue
        cnt += 1
        if cnt==M: return n
        n += 1
    return 0

print(main())