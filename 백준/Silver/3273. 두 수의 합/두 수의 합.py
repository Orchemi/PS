import sys
input = sys.stdin.readline

N = int(input())
arr = set(map(int, input().split()))
M = int(input())

cnt = 0
for a in arr:
    if M-a in arr: cnt += 1

print(cnt//2)