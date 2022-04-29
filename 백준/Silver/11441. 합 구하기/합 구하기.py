import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
i = 1
while i <= N:
    arr[i] += arr[i-1]
    i += 1

M = int(input())
for _ in range(M):
    s, e = map(int, input().split())
    print(arr[e]-arr[s-1])