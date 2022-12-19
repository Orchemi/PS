def main():
    N = int(input())
    Q = []
    for _ in range(N):
        t, e = map(int, input().split())
        Q.append((e, t))
    Q.sort()

    tt = 0
    ret = 1e8
    for i in range(N):
        e, t = Q[i]
        if tt+t > e: return -1
        tt += t
        ret = min(ret, e-tt)
    return ret

print(main())