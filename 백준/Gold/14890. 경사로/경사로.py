def main(arr):
    global N, L
    check = [0]*N
    std = arr[0]

    def check_float(part):
        global N, L
        std = part[0]
        for p in part:
            if p != std: return 0
        return 1

    i = 1
    while i < N:
        # 높이차가 1 이상
        if abs(arr[i]-std) > 1: return 0
        # 높이가 같음
        elif arr[i]==std: i+=1
        # 높이가 1 작아짐
        elif arr[i]+1 == std:
            if i+L > N: return 0
            if not check_float(arr[i:i+L]): return 0
            for k in range(i, i+L):
                check[k] = 1
            i += L
            std -= 1

        # 높이가 1 높아짐
        elif arr[i]-1 == std:
            if i-L < 0: return 0
            # 1. 뒤의 경사로 구간이 모두 평평한지 체크
            if not check_float(arr[i-L:i]): return 0
            # 2. 뒤에 경사로가 없었는지 체크
            for k in range(i-L, i):
                if check[k]: return 0
            for k in range(i-L, i):
                check[k] = 1
            i += 1
            std += 1

    return 1


N, L = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    road = mat[i]
    ans += main(road)

for j in range(N):
    road = []
    for i in range(N):
        road.append(mat[i][j])
    ans += main(road)

print(ans)