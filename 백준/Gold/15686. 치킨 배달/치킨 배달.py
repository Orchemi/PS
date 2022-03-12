import sys
input = sys.stdin.readline

def pick(i, s, M):
    global chickens, chickensAlive
    global visited, ans
    if i == M:
        ans = min(ans, calcDistance(chickensAlive))
        return

    for k in range(s, chickensCnt):
        if not visited[k]:
            visited[k] = 1
            chickensAlive.append(chickens[k])
            pick(i+1, k+1, M)
            visited[k] = 0
            chickensAlive.pop()


def calcDistance(chickensAlive):
    global houses

    summin_d = 0
    for house in houses:
        hi, hj = house
        d_lst = []
        for chicken in chickensAlive:
            ci, cj = chicken
            d = abs(ci-hi) + abs(cj-hj)
            d_lst.append(d)
        summin_d += min(d_lst)

    return summin_d


N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

chickens = []
chickensCnt = 0
houses = []
for i in range(N):
    for j in range(N):
        if mat[i][j]==1:
            houses.append((i, j))
        elif mat[i][j]==2:
            chickens.append((i, j))
            chickensCnt += 1

visited = [0]*chickensCnt
chickensAlive = []
ans = 1000000
pick(0, 0, M)
print(ans)