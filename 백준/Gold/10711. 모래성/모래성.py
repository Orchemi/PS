I, J = map(int, input().split())
mat = [list(map(lambda x: (x if x=='.' else int(x)), input())) for _ in range(I)]
cass = [[[0xfff, 0] for _ in range(J)] for _ in range(I)]

# 최초 높이 계산
Q = set()
ql = 0
for i in range(I):
    for j in range(J):
        if mat[i][j]!='.':
            cass[i][j][0] = int(mat[i][j])
            Q.add((i, j))
            ql += 1


# 모두 모래라면 0 출력
if not Q:
    print(0)
    quit()

# 최초 removeSet 확인
removeSet = set()
while Q:
    ni, nj = Q.pop()
    cnt = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            si, sj = ni+di, nj+dj
            if mat[si][sj]=='.':
                cnt += 1

    cass[ni][nj][1] = cnt
    if cnt >= cass[ni][nj][0]:
        removeSet.add((ni, nj))

wave = 0
while removeSet:
    removeSet2 = removeSet
    removeSet = set()
    while removeSet2:
        ni, nj = removeSet2.pop()
        mat[ni][nj] = '.'

        for di in range(-1, 2):
            for dj in range(-1, 2):
                si, sj = ni+di, nj+dj
                if mat[si][sj]=='.': continue
                cass[si][sj][1] += 1

                if cass[si][sj][0] == cass[si][sj][1]:

                    removeSet.add((si, sj))

    wave += 1

print(wave)