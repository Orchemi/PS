tcs = int(input())

for tc in range(tcs):
    r, S = input().split()
    R = int(r)

    for char in S:
        print(f'{char*R}', end='')

    print()