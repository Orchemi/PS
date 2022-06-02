import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
sum_lst = [0]*(N+1)

for i in range(1, N+1):
    sum_lst[i] = sum_lst[i-1] + arr[i-1]

ans = 100001
s = 0
e = 1

while s!=N:
    if sum_lst[e] - sum_lst[s] >= S:
        if e-s < ans:
            ans = e-s
        s += 1

    else:
        if e != N:
            e += 1
        else:
            s += 1

print(ans) if ans < 100001 else print(0)