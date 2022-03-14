import sys
sys.setrecursionlimit(10000)

def fact(n):
    global memo, memoL

    if n > memoL:
        memo.append(n * fact(n-1))
        memoL += 1

    elif n == memoL:
        memo.append(n * memo[n-1])
        memoL += 1

    return memo[n]


memo = [1, 1]
memoL = 2

n = int(input())
k = (n+1)//2
sum_v = 0
i = 0
for m in range(n, k-1, -1):
    val = fact(m) // (fact(i) * fact(m-i))
    sum_v += val
    i += 1

print(sum_v % 10007)