def put_bomb():
    global I, J, mat, t
    for i in range(I):
        for j in range(J):
            if not mat[i][j]:
                mat[i][j] = t

def print_mat():
    global I, J, mat
    for i in range(I):
        for j in range(J):
            mat[i][j] = 'O' if mat[i][j] else '.'
    for l in mat:
        print(*l, sep="")

def boom():
    global I, J, mat, t, boom_soon_list

    def boom_one(i, j):
        global I, J, mat
        for di, dj in ((0,0),(-1,0),(1,0),(0,1),(0,-1)):
            si, sj = i+di, j+dj
            if not (0<=si<I and 0<=sj<J): continue
            boom_soon_list.add((si, sj))

    for i in range(I):
        for j in range(J):
            if mat[i][j] == t-3:
                bomb_list.add((i, j))

    while bomb_list:
        bi, bj = bomb_list.pop()
        boom_one(bi, bj)

    while boom_soon_list:
        bi, bj = boom_soon_list.pop()
        mat[bi][bj] = 0

I, J, N = map(int, input().split())
D = {1:2, 2:1}
bomb_list = set()
boom_soon_list = set()
t = -1
mat = []
for _ in range(I):
    lst = list(input())
    mat.append([])
    for k in lst:
        mat[-1].append(0 if k=='.' else -1)

t += 2
if N==1:
    print_mat()
    quit()

put_bomb()
t += 1
if N==2:
    print_mat()
    quit()

while t < N:
    put_bomb() if t%2 else boom()
    t += 1

print_mat()