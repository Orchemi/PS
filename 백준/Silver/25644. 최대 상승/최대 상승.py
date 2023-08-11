def main():
    N = int(input())
    arr = list(map(int, input().split()))
    ret = 0
    maxx = minn = arr[N-1]
    i = N-2
    while i >= 0:
        cur = arr[i]
        if cur > maxx:
            ret = max(ret, maxx-minn)
            maxx = minn = cur
        elif cur < minn:
            minn = cur
        i -= 1

    return max(ret, maxx-minn)

print(main())