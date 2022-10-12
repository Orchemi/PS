def main(N):
    D = {}
    n = 2
    while N > 1:
        if N%n:
            n += 1
        else:
            D[n] = D.get(n, 0) + 1
            N = N//n
    return D

T = int(input())
for _ in range(T):
    N = int(input())
    ret = main(N)
    for k in sorted(ret.keys()):
        print(k, ret[k])