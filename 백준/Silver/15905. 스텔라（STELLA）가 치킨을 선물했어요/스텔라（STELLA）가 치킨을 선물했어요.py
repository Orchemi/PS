def main():
    N = int(input())
    arr = sorted([list(map(int, input().split())) for _ in range(N)], key=(lambda x: (-x[0], x[1])))
    n, s = arr[4]
    cnt = 0
    for i in range(5, N):
        if arr[i][0] == n:
            cnt += 1
        else:
            return cnt
    return cnt

print(main())