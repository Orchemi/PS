import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)])
ret = 0
for n in range(N):
    ret += abs(arr[n] - (n+1))

print(ret)