T = int(input())
for _ in range(T):
    N = int(input())
    S = set(map(int, input().split()))
    M = int(input())
    arr = list(map(int, input().split()))
    for a in arr:
        print(1 if a in S else 0)