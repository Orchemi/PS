import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())

    set1 = set(range(x, M*N+1, M))
    set2 = set(range(y, M*N+1, N))
    set3 = set1 & set2

    if not set3:
        print(-1)
        continue
    print(min(set3))