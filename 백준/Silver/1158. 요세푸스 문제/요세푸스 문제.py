N, K = map(int, input().split())
arr = list(range(1, N+1))
cur_i = K-1
ret = []

while N:
    while cur_i < N:
        ret.append(arr.pop(cur_i))
        cur_i += K-1
        N -= 1
    cur_i -= N

print(f'<{", ".join([str(n) for n in ret])}>')