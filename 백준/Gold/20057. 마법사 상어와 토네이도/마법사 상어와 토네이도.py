import sys
input = sys.stdin.readline

def move_line():
    global ci, cj, direction, try_cnt
    for _ in range((try_cnt + 2) // 2):
        di, dj = direction[try_cnt % 4]
        move_one(di, dj)
        ci += di
        cj += dj
    try_cnt += 1

def move_one(di, dj):
    global ci, cj, try_cnt, direction, mat
    if ci == cj == 0: return
    stdi, stdj = ci+di, cj+dj
    stdv = mat[stdi][stdj]
    mat[stdi][stdj] = 0
    p1 = int(stdv*0.01)
    p2 = int(stdv*0.02)
    p5 = int(stdv*0.05)
    p7 = int(stdv*0.07)
    p10 = int(stdv*0.10)
    last = stdv - 2*(p1+p2+p7+p10) - p5

    # 위아래 이동
    if try_cnt%2:
        check(stdi, stdj+1, p7)
        check(stdi, stdj-1, p7)
        check(stdi, stdj+2, p2)
        check(stdi, stdj-2, p2)
        check(stdi+di, stdj+1, p10)
        check(stdi+di, stdj-1, p10)
        check(stdi-di, stdj+1, p1)
        check(stdi-di, stdj-1, p1)
        check(stdi+di*2, stdj, p5)
        check(stdi + di, stdj, last)

    # 왼쪽 오른쪽 이동
    else:
        check(stdi+1, stdj, p7)
        check(stdi-1, stdj, p7)
        check(stdi+2, stdj, p2)
        check(stdi-2, stdj, p2)
        check(stdi+1, stdj+dj, p10)
        check(stdi-1, stdj+dj, p10)
        check(stdi+1, stdj-dj, p1)
        check(stdi-1, stdj-dj, p1)
        check(stdi, stdj+dj*2, p5)
        check(stdi, stdj + dj, last)

def check(i, j, v):
    global global_ans, mat, N
    if 0<=i<N and 0<=j<N:
        mat[i][j] += v
    else:
        global_ans += v

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

direction = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0)
}
try_cnt = 0
ci = cj = N//2
global_ans = 0

move_line()
while not (ci==0 and cj==-1):
    for _ in range(4):
        move_line()

print(global_ans)