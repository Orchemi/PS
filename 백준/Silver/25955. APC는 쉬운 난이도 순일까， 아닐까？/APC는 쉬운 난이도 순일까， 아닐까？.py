def main():
    def convert(t):
        return D[t[0]]*10**4 + (1000-int(t[1:]))

    def reconvert(n):
        a, b = n//10000, n%10000
        return f'{E[a]}{1000-b}'

    N = int(input())
    D = {
        'B': 1,
        'S': 2,
        'G': 3,
        'P': 4,
        'D': 5,
    }
    E = ['', 'B', 'S', 'G', 'P', 'D']

    T1 = list(input().split())
    N1 = [convert(t) for t in T1]
    N2 = sorted(N1)
    R = []
    for n in range(N):
        if N1[n] == N2[n]: continue
        R.append(N1[n])
    T2 = [reconvert(n) for n in sorted(R)]
    if T2:
        print('KO')
        print(*T2)
    else:
        print('OK')

main()