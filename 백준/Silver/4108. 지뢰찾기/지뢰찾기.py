while True:
    I, J = map(int, input().split())
    if I==0 and J==0: break
    mat = [list(input()) for _ in range(I)]
    ret = [[0]*J for _ in range(I)]

    for i in range(I):
        for j in range(J):
            if mat[i][j]=='*':
                ret[i][j] = '*'
                continue

            cnt = 0
            for di in range(-1, 2):
                si = i+di
                if not (0<=si<I): continue
                for dj in range(-1, 2):
                    sj = j+dj
                    if not (0<=sj<J): continue
                    if di==0 and dj==0: continue
                    if mat[si][sj]=='*':
                        cnt += 1
            ret[i][j] = cnt

    for l in ret:
        print(*l, sep='')