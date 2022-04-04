import sys
input = sys.stdin.readline

def main1(i, ni, nj, ssum):
    global visited
    if i==4:
        global maxV
        maxV = max(maxV, ssum)
        return

    for di, dj in didj:
        si, sj = ni+di, nj+dj
        if not (0<=si<I and 0<=sj<J): continue
        if visited[si][sj]: continue
        visited[si][sj] = 1
        main1(i+1, si, sj, ssum+mat[si][sj])
        visited[si][sj] = 0

def main2(ni, nj):
    global maxV

    arr = []
    for di, dj in didj:
        si, sj = ni+di, nj+dj
        if not (0<=si<I and 0<=sj<J): continue
        arr.append(mat[si][sj])

    l = len(arr)
    val = mat[ni][nj]
    if l==4:
        val += sum(arr) - min(arr)
        maxV = max(maxV, val)
    elif l==3:
        val += sum(arr)
        maxV = max(maxV, val)
    return

I, J = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(I)]
visited = [[0]*J for _ in range(I)]
didj = ((-1,0),(1,0),(0,-1),(0,1))

maxV = 0
for i in range(I):
    for j in range(J):
        visited[i][j] = 1
        main1(1, i, j, mat[i][j])
        visited[i][j] = 0
        main2(i, j)

print(maxV)