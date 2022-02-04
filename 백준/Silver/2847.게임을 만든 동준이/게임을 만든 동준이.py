import sys

n = int(sys.stdin.readline())
point = [int(sys.stdin.readline()) for _ in range(n)]
point.reverse()
target = point[0]
res = []
for i in range(1, n):
    if target <= point[i]:
        cnt = - (target - point[i] - 1)
        point[i] -= cnt
        res.append(cnt)

    target = point[i]

print(sum(res))