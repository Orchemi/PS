def main(i):
    global N, V
    if i==N-1:
        for j in range(N):
            if j in V: continue
            if j-i in R: continue
            if j+i in L: continue
            return 1
        return 0

    cnt = 0
    for j in range(N):
        if j in V: continue
        if j-i in R: continue
        if j+i in L: continue

        V.add(j)
        R.add(j-i)
        L.add(j+i)

        cnt += main(i+1)

        V.remove(j)
        R.remove(j-i)
        L.remove(j+i)

    return cnt

N = int(input())
V, R, L = set(), set(), set()
print(main(0))