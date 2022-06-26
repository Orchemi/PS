N, A = map(int, input().split())
ans = 0
while N:
    N = N//A
    ans += N

print(ans)