import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def main(n):
    global memo
    if memo[0][n]: return memo[0][n]
    if not memo[0][n-1]:
        main(n-1)

    check123(n)
    calc0(n)

    return memo[0][n]

def check123(n):
    global memo
    d = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2]
    }

    for i in range(1, 4):
        for j in d[i]:
            memo[i][n] += memo[j][n-i]
        memo[i][n] = memo[i][n]%1000000009

def calc0(n):
    global memo
    memo[0][n] = (memo[1][n] + memo[2][n] + memo[3][n]) % 1000000009


memo = [[0]*1000001 for _ in range(4)]

memo[1][1] = memo[2][2] = memo[3][3] = 1
calc0(1)
calc0(2)

T = int(input())
for _ in range(T):
    n = int(input())
    print(main(n))