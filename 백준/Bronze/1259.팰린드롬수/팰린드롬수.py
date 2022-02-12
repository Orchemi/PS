while True:
    N = input()
    if N == '0':
        quit()
    elif N == N[::-1]:
        print('yes')
    else:
        print('no')