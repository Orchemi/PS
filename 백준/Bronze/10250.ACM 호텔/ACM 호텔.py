tcs = int(input())

for tc in range(tcs):
    H, W, N = map(int, input().split())

    if (N % H) == 0:
        c = (N // H)
        r = H
    else:
        c = (N // H) + 1
        r = N % H

    print(f'{r}{c:02}')