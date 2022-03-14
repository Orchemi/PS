import sys
input = sys.stdin.readline

def dfs(i, N):
    global didj_dict
    if i == N:
        findStart()
        return

    ci, cj, ck = CCTVs[i]
    for didj_lst in didj_dict[ck]:
        cctvSet.append((ci, cj, didj_lst))
        dfs(i+1, N)
        cctvSet.pop()


def findStart():
    global cctvSet, mat, min_ns
    global I, J

    # mat2 제작
    mat2 = []
    for lst in mat:
        mat2.append(lst[::])

    # 모든 CCTV의 감시지역 체크
    for cctvInfo in cctvSet:
        ci, cj, didj_lst = cctvInfo
        for di, dj in didj_lst:
            k = 1
            while 0<=ci+di*k<I and 0<=cj+dj*k<J:
                # 탐색 좌표의 값이 0이면 # 넣기
                if not mat2[ci+di*k][cj+dj*k]:
                    mat2[ci+di*k][cj+dj*k] = '#'
                # 탐색 좌표의 값이 6이면 반복 탈출
                elif mat2[ci+di*k][cj+dj*k]==6:
                    break

                k += 1
    # mat2의 0 체크
    sum_v = 0
    for i in range(I):
        for j in range(J):
            if not mat2[i][j]:
                sum_v += 1

    # sum_v = 0이면 종료
    if not sum_v:
        print(0)
        quit()

    # 최솟값 갱신
    if min_ns > sum_v:
        min_ns = sum_v



# 입력 처리
I, J = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(I)]
didj_dict = {
    1: [[(-1,0)],
        [(0,-1)],
        [(1,0)],
        [(0,1)]],
    2: [[(-1,0),(1,0)],
        [(0,-1),(0,1)]],
    3: [[(0,-1),(-1,0)],
        [(-1,0),(0,1)],
        [(0,1),(1,0)],
        [(1,0),(0,-1)]],
    4: [[(-1,0),(0,1),(1,0)],
        [(0,-1),(0,1),(1,0)],
        [(0,-1),(-1,0),(1,0)],
        [(0,-1),(-1,0),(0,1)]],
    5: [[(0,-1),(-1,0),(0,1),(1,0)]]}

# CCTV 좌표, 종류 저장
cctvN = 0
CCTVs = []
for i in range(I):
    for j in range(J):
        if 0 < mat[i][j] < 6:
            CCTVs.append((i, j, mat[i][j]))
            cctvN += 1

# main 실행
cctvSet = []
min_ns = I*J
dfs(0, cctvN)

# 결과 출력
print(min_ns)