N = int(input())
X = 10 if N < 8 else N
memo = [0]*(X+1)
memo[2] = 1
k = 5
while k <= N:
    flag = 1
    for i in (1, 3, 4):
        if memo[k-i]:
            flag = 0
            break

    if flag: memo[k] = 1
    k += 1

ret = 'CY' if memo[N] else 'SK'
print(ret)