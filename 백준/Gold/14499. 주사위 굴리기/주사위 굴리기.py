I, J, ni, nj, K = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(I)]
movearr = list(map(lambda x:int(x)-1, input().split()))
movedelta = ((0,1),(0,-1),(-1,0),(1,0))
c = [0]*6

for nd in movearr:
    di, dj = movedelta[nd]
    si, sj = ni+di, nj+dj
    if not (0<=si<I and 0<=sj<J): continue

    # 값 바꾸기
    if mat[si][sj]:
        c[nd] = mat[si][sj]
        mat[si][sj] = 0
    else:
        mat[si][sj] = c[nd]

    # 큐브 재배치
    if nd==0:
        c[1], c[5], c[0], c[4] = c[5], c[0], c[4], c[1]

    elif nd==1:
        c[5], c[0], c[4], c[1] = c[1], c[5], c[0], c[4]

    elif nd==2:
        c[3], c[5], c[2], c[4] = c[5], c[2], c[4], c[3]

    else:
        c[5], c[2], c[4], c[3] = c[3], c[5], c[2], c[4]

    print(c[4])
    ni, nj = si, sj