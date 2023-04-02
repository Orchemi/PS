N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    for _ in range(b):
        print('X'*a)
    print()