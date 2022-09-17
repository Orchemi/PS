import sys
input = sys.stdin.readline

# 지훈, 불 위치 찾기
def find_JF():
    global mat, I, J
    for i in range(I):
        for j in range(J):
            if mat[i][j] == 'F':
                F_set.add((i, j))
            elif mat[i][j] == 'J':
                J_set.add((i, j))

# 지훈 이동
def move_JH():
    global mat, I, J, J_set
    tmp = set()
    while J_set:
        ni, nj = J_set.pop()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            si, sj = ni+di, nj+dj
            if not (0<=si<I and 0<=sj<J): return True
            if mat[si][sj] == '.':
                mat[si][sj] = 'J'
                tmp.add((si, sj))
    J_set = tmp

def move_fire():
    global mat, I, J, F_set, J_set
    tmp = set()
    while F_set:
        ni, nj = F_set.pop()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            si, sj = ni+di, nj+dj
            if not (0<=si<I and 0<=sj<J): continue
            if mat[si][sj] == '#': continue
            if mat[si][sj] == 'F': continue
            mat[si][sj] = 'F'
            J_set -= {(si, sj)}
            tmp.add((si, sj))
    F_set = tmp

I, J = map(int, input().split())
mat = [list(input()) for _ in range(I)]
J_set, F_set = set(), set()
find_JF()

time = 0
impossible = 0
while True:
    time += 1
    if move_JH(): break
    move_fire()
    if not J_set:
        impossible = 1
        break

print('IMPOSSIBLE') if impossible else print(time)