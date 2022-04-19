import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)

maxW = 0
i = 0
while i < N:
    if maxW < arr[i]*(i+1):
        maxW = arr[i]*(i+1)
    i += 1
print(maxW)