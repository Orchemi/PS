def main():
    N = int(input())-1
    T = 1
    op = 0

    while True:
        if T*2 > N: break
        T *= 2

    while T:
        if T <= N:
            N -= T
            op ^= 1
        T = T//2

    return op

print(main())