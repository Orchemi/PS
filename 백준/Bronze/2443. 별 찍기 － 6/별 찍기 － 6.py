def main(n, s):
    if not n: return
    for _ in range(s):
        print(' ', end='')
    for _ in range(n*2-1):
        print('*', end='')
    print()
    main(n-1, s+1)

N = int(input())
main(N, 0)