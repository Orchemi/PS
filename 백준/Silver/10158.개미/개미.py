def func(T, n, L):
    T = T % (2 * L)
    if T == 0:
        return n

    if T >= L - n:
        T -= (L - n)
        n = L
    else:
        return n + T

    if T >= L:
        T -= L
        return T
    else:
        return n - T

I, J = map(int, input().split())
ni, nj = map(int, input().split())
di, dj = 1, 1
ai, aj = -1, -1
T = int(input())
print(func(T, ni, I), func(T, nj, J))