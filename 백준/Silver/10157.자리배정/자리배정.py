D = {
    0:(0,1),
    1:(1,0),
    2:(0,-1),
    3:(-1,0)
}


R, C = map(int, input().split())
N = int(input())

if N > R*C:
    print(0)
    quit()

ni, nj = 0, 0

n = 1
i = 1
while n + 2*(R+C+2-4*i) < N:
    n += 2*(R+C+2-4*i)
    i += 1


d = 0
ni, nj = 0, 0
di, dj = D[d%4]

C2 = C-2*(i-1)
R2 = R-2*(i-1)
mat = [[0]*C2 for _ in range(R2)]

while n < N:
    mat[ni][nj] = n
    if 0<=ni+di<R2 and 0<=nj+dj<C2:
        if mat[ni+di][nj+dj]:
            d+=1
            di, dj = D[d%4]
    else:
        d += 1
        di, dj = D[d%4]

    ni += di
    nj += dj
    n += 1

print(i+ni, i+nj)