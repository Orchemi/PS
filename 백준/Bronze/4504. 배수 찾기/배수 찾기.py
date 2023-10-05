N = int(input())
while True:
    M = int(input())
    if not M: break
    print(f'{M} is {"NOT " if M%N else ""}a multiple of {N}.')