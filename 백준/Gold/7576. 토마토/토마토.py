import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
# sys.stdin = open('t.txt')


def isThereZero():
    global mat, H, W

    for i in range(H):
        for j in range(W):
            if not mat[i][j]:
                return 1
    return 0


def bfs(days, ni, nj):
    global Q, H, W, end, ans
    global mat
    didj = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for di, dj in didj:
        if 0<=ni+di<H and 0<=nj+dj<W:
            if not mat[ni+di][nj+dj]:
                mat[ni+di][nj+dj] = days+1

                if ans < days+1:
                    ans = days+1

                Q.append((days+1, ni+di, nj+dj))
                end += 1


W, H = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(H)]

# 0. 0이 없으면 0 출력
if not isThereZero():
    print(0)
    quit()

# 1. 모든 1의 좌표와 depth(0)를 Q에 넣음
start = -1
end = 0
Q = []
for i in range(H):
    for j in range(W):
        if mat[i][j]==1:
            Q.append((0, i, j))
            end += 1

# 2. 계산
ans = 0
while start < end-1:
    start += 1
    days, ni, nj = Q[start]
    bfs(days, ni, nj)

# 3. 0 있는지 확인
if isThereZero():
    print(-1)
    quit()

# 4. ans 출력
print(ans)

