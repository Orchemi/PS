import sys
input = sys.stdin.readline

def BFS(i, j):
    visited = [[0]*J for _ in range(I)]
    didj = [(-1,0),(1,0),(0,1),(0,-1)]
    visited[i][j] = 1
    Q = [(i, j)]
    front = -1
    rear = 0
    max_now = 0
    while front < rear:
        front += 1
        ni, nj = Q[front]
        for di, dj in didj:
            si, sj = ni+di, nj+dj
            if not (0<=si<I and 0<=sj<J): continue
            if visited[si][sj]: continue
            if not mat[si][sj]: continue
            visited[si][sj] = visited[ni][nj]+1
            max_now = max(visited[si][sj], max_now)
            Q.append((si, sj))
            rear += 1
    return max_now-1


I, J = map(int, input().split())
mat = []
for _ in range(I):
    l = [1 if i=='L' else 0 for i in list(input())]
    mat.append(l)

max_val = 0
for i in range(I):
    for j in range(J):
        if not mat[i][j]: continue
        val = BFS(i, j)
        if max_val < val:
            max_val = val
print(max_val)