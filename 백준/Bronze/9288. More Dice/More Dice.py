T = int(input())
for t in range(1, T+1):
    N = int(input())
    print(f'Case {t}:')
    if N > 7:
        b, a = 6, N-6
    else:
        a, b = 1, N-1

    while a <= b:
        print(f'({a},{b})')
        a, b = a+1, b-1