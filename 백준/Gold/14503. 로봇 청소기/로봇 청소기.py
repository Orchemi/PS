import sys; input = sys.stdin.readline

search = {
    0: [0, -1],
    1: [-1, 0],
    2: [0, 1],
    3: [1, 0]
}

back = {
    0: [1, 0],
    1: [0, -1],
    2: [-1, 0],
    3: [0, 1]
}

def turn(i, nd):
    global search
    global ni, nj

    if i == 4:
        return -1

    di, dj = search[nd%4]
    if mat[ni+di][nj+dj]==0:
        return nd%4
    else:
        return turn(i+1, nd-1)


H, W = map(int, input().split())
ni, nj, nd = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(H)]

mat[ni][nj] = 2
cnt = 1
ON = 1
while ON:
    pd = turn(0, nd)
    if pd < 0:
        bi, bj = back[nd%4]
        if mat[ni+bi][nj+bj]==1:
            ON = 0
        else:
            ni += bi
            nj += bj
    else:
        nd = pd
        di, dj = search[nd%4]
        ni += di
        nj += dj
        mat[ni][nj] = 2
        cnt += 1
        nd -= 1

print(cnt)