def dfs(i, ssum):
    if i==N:
        return 0 if ssum%3 else 1

    cnt = 0
    for j in range(3):
        cnt += dfs(i+1, ssum+j)
    return cnt

cnt = 0
N = int(input())
for j in range(1, 3):
    cnt += dfs(1, j)
print(cnt)