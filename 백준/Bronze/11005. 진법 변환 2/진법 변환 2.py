N, K = map(int, input().split())
ret = ''
while N:
    N, n = N//K, N%K
    head = chr(55+n) if n > 9 else str(n)
    ret = head+ret
print(ret)