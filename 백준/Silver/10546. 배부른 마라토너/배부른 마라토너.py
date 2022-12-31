import sys
input = sys.stdin.readline

def main():
    N = int(input())
    S = {}
    for _ in range(N):
        name = input()
        S[name] = S.get(name, 0) + 1

    D = {}
    for _ in range(N-1):
        name = input()
        D[name] = D.get(name, 0)+1

    for k, v in S.items():
        if D.get(k, 0) != S.get(k, 0): return k

print(main())