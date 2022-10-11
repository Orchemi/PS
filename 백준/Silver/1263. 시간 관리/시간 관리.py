def main():
    N = int(input())
    min_t = 1e6
    now = 0
    arr = []
    for _ in range(N):
        t, s = map(int, input().split())
        arr.append([t, s])
    arr.sort(key=lambda x:(x[1]))

    for t, s in arr:
        now += t
        if now > s: return -1

        if min_t > s-now:
            min_t = s - now
    return min_t

print(main())