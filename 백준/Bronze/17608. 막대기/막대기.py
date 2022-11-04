import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
cnt, cv, ci = 0, 0, N-1
while ci >= 0:
    if cv < arr[ci]:
        cv = arr[ci]
        cnt += 1
    ci -= 1
print(cnt)