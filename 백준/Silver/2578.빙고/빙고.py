matC = [list(map(int, input().split())) for _ in range(5)]
lstA = []
for _ in range(5):
    lstA += list(map(int, input().split()))

cnt = 0
for a in lstA:
    bingo = 0
    cnt += 1
    for i in range(5):
        for j in range(5):
            if matC[i][j] == a:
                matC[i][j] = 0

    for i in range(5):
        if matC[i] == [0, 0, 0, 0, 0]:
            bingo += 1

    for j in range(5):
        b = 0
        for i in range(5):
            b += matC[i][j]
        if b == 0:
            bingo += 1

    b = 0
    for k in range(5):
        b += matC[k][k]
    if b == 0:
        bingo += 1

    b = 0
    for k in range(5):
        b += matC[k][4-k]
    if b == 0:
        bingo += 1

    if bingo >= 3:
        print(cnt)
        quit()

print(bingo)