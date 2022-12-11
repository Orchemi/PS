def main():
    N = int(input())
    if N%2: return 0
    M = max(N+1, 3)
    T = [0]*M
    T[2] = 3

    i = 4
    acc = 1
    while i<=N:
        T[i] = 3*T[i-2] + 2*acc
        acc += T[i-2]
        i += 2
    return T[N]

print(main())