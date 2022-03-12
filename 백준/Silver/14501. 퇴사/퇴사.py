def dfs(i):
    global max_price, sum_val
    global N, lst

    if i >= N:
        if max_price < sum_val:
            max_price = sum_val
        return

    for k in range(i, N):
        day, price = lst[k]

        if k + day <= N:
            sum_val += price
            dfs(k+day)
            sum_val -= price
        else:
            dfs(k+day)


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
max_price = 0
sum_val = 0
dfs(0)
print(max_price)