N, M = map(int, input().split())
J = int(input())
ret = 0

p = 1
for _ in range(J):
    k = int(input())
    if k < p:
        ret += p-k
        p = k
    elif k > p+M-1:
        ret += k-(p+M-1)
        p = k-M+1
print(ret)