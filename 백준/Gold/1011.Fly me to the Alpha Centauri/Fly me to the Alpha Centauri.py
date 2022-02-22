tcs = int(input())
for tc in range(tcs):
    A, B = map(int, input().split())
    d = B-A
    move = 0
    flag = 0
    v = 0

    while d > 0:
        if flag == 0:
            v += 1
            d -= v
            move += 1
            flag += 1

        elif flag == 1:
            d -= v
            move += 1
            flag -= 1

    print(move)