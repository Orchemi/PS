T = int(input())
ans = [300, 60, 10]

for i in range(3):
    T, ans[i] = T%ans[i], T//ans[i]

print(-1) if T else print(*ans)