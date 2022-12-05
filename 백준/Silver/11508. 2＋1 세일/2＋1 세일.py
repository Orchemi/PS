import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)])
K = N//3
ret = 0
for _ in range(K):
    ret += arr.pop()
    ret += arr.pop()
    arr.pop()

ret += sum(arr)
print(ret)