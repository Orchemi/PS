N, K = map(int, input().split())
lst = [0]*12

for _ in range(N):
    s, g = map(int, input().split())
    lst[s*6+g-1] += 1

ans = 0
for n in lst:
    if n%K:
        ans += 1
    ans += n//K

print(ans)