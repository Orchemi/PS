import sys
input = sys.stdin.readline

# 하나라도 0이 있으면 True, 아니면 False
def checkZero():
    global cube, H, I, J
    for h in range(H):
        for i in range(I):
            for j in range(J):
                if not cube[h][i][j]:
                    return 1
    return 0


# 입력 처리
J, I, H = map(int, input().split())
cube = []
for _ in range(H):
    mat = [list(map(int, input().split())) for _ in range(I)]
    cube.append(mat)

# 저장될 때부터 모두 익으면(0이 없으면) 0 출력
if not checkZero():
    print(0)
    quit()

# 1의 좌표를 Q에 삽입
Q = []
front, back = -1, 0
for h in range(H):
    for i in range(I):
        for j in range(J):
            if cube[h][i][j]==1:
                Q.append((0, h, i, j))
                back += 1


# 숙성 시작
max_day = 0
while front < back-1:
    front += 1
    nday, nh, ni, nj = Q[front]

    dhij = [(0,-1,0), (0,1,0), (0,0,-1), (0,0,1), (1,0,0), (-1,0,0)]
    for dh, di, dj in dhij:
        # 탐색 방향이 상자 범위 이내이고
        if (0<=nh+dh<H) and (0<=ni+di<I) and (0<=nj+dj<J):
            # 안 익은 토마토라면
            if not cube[nh+dh][ni+di][nj+dj]:
                # cube에 탐색 위치를 체크
                cube[nh+dh][ni+di][nj+dj] = 1
                # Q에 탐색 좌표와 일수를 추가
                Q.append((nday+1, nh+dh, ni+di, nj+dj))
                back += 1

                if max_day < nday+1:
                    max_day = nday+1

# 숙성 모두 마치고 안 익은 토마토가 있다면 -1 출력, 아니라면 max_day 출력
print(-1 if checkZero() else max_day)