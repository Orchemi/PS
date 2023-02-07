def main():
    N = int(input())
    M = N**2
    Ns, Ms = str(N), str(M)
    l = len(Ns)
    return 'YES' if Ms[-l:] == Ns else 'NO'

for _ in range(int(input())):
    print(main())