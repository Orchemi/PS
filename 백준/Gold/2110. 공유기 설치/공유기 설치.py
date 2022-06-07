import sys
input = sys.stdin.readline

def binary_search():
    global houses, ans, N, C
    s, e = 1, houses[-1] - houses[0]
    while s <= e:
        m = (s + e) // 2
        cur = houses[0]
        cnt = 1
        i = 1
        for i in range(1, N):
            if houses[i] >= cur + m:
                cnt += 1
                cur = houses[i]

        if cnt < C:
            e = m-1
            continue

        s = m+1
        ans = m

N, C = map(int, input().split())
houses = sorted([int(input()) for _ in range(N)])
ans = 0
binary_search()
print(ans)