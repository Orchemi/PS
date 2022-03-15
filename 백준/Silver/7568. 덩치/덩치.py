import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    w, h = map(int, input().split())
    arr.append([w, h])

arr2 = []
for i in range(N):
    nw, nh = arr[i]
    cnt = 1

    for j in range(N):
        tw, th = arr[j]
        if nw < tw and nh < th:
            cnt += 1

    arr2.append(cnt)

print(*arr2)