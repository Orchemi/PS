while True:
    N = input()
    if N == '0':
        break

    while len(N) > 1:
        if N[0] == N[-1]:
            flag = 1
            N = N[1:-1]
        else:
            print('no')
            break

    if len(N) <= 1:
        print('yes')