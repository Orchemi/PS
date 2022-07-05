N, L = map(int, input().split())
arr = sorted(list(map(int, input().split())))

cur = 0
cnt = 0
for a in arr:
    if a+0.5 > cur:
        cnt += 1
        cur = a-0.5+L

print(cnt)