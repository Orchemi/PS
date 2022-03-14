import sys
input = sys.stdin.readline

def checkArea(i, j):
    global mat, total, areas, I, J
    Q = [(i, j)]
    size = 1
    start = -1
    end = 1
    didj = [(-1,0),(1,0),(0,-1),(0,1)]
    mat[i][j] = 1

    while start < end-1:
        start += 1
        ni, nj = Q[start]
        for di, dj in didj:
            if 0<=ni+di<I and 0<=nj+dj<J:
                if not mat[ni+di][nj+dj]:
                    mat[ni+di][nj+dj] = 1
                    Q.append((ni+di, nj+dj))
                    size += 1
                    end += 1
    return size

# 입력
J, I, K = map(int, input().split())
mat = [[0]*J for _ in range(I)]

# 범위에 체크
for _ in range(K):
    i1, j1, i2, j2 = list(map(int, input().split()))
    for i in range(i1, i2):
        for j in range(j1, j2):
            mat[i][j] = 1

# 완전탐색
total = 0
areas = []
for i in range(I):
    for j in range(J):
        if not mat[i][j]:
            areas.append(checkArea(i, j))
            total += 1

print(total)
print(*sorted(areas))