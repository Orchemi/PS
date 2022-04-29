import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def f(n):
    global memo, arr
    if not n: return 0
    if not memo[n]:
        memo[n] = arr[n] + f(n-1)
    return memo[n]


N = int(input())
arr = [0] + list(map(int, input().split()))
memo = [0]*(N+1)
memo[1] = arr[1]
M = int(input())
for _ in range(M):
    s, e = map(int, input().split())
    print(f(e) - f(s-1))