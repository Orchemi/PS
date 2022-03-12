import sys
input = sys.stdin.readline


def diffusionMain():
    global I, J, AU, AD
    global mat
    matNew = [[0]*J for _ in range(I)]
    didj = [(-1,0),(1,0),(0,-1),(0,1)]
    for i in range(I):
        for j in range(J):
            matNew[i][j] += mat[i][j]
            if matNew[i][j] > 4:
                v = mat[i][j] // 5
                for di, dj in didj:
                    if 0<=i+di<I and 0<=j+dj<J:
                        if mat[i+di][j+dj] > -1:
                            matNew[i+di][j+dj] += v
                            matNew[i][j] -= v

    return matNew


def cleanAirUp():
    global I, J, AU, AD
    global mat, ni, nj

    ni, nj = AU - 1, 0
    while ni-1 >= 0:
        mat[ni][0] = mat[ni-1][0]
        ni -= 1

    mat[0][0:-1] = mat[0][1:]

    ni = 0
    while ni+1 <= AU:
        mat[ni][J-1] = mat[ni+1][J-1]
        ni += 1

    mat[AU][2:] = mat[AU][1:-1]

    mat[AU][1] = 0


def cleanAirDown():
    global I, J, AU, AD
    global mat, ni, nj

    ni, nj = AD+1, 0
    while ni+1 <= I-1:
        mat[ni][0] = mat[ni+1][0]
        ni += 1

    mat[I-1][0:-1] = mat[I-1][1:]

    ni = I-1
    while ni-1 >= AD:
        mat[ni][J-1] = mat[ni-1][J-1]
        ni -= 1

    mat[AD][2:] = mat[AD][1:-1]

    mat[AD][1] = 0


I, J, T = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(I)]

for i in range(I):
    if mat[i][0]==-1:
        AU, AD = i, i+1
        break

t = 0
while t < T:
    mat = diffusionMain()
    cleanAirUp()
    cleanAirDown()
    t += 1

ret = 0
for i in range(I):
    for j in range(J):
        if mat[i][j] > 0:
            ret += mat[i][j]
print(ret)