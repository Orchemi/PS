import sys
input = sys.stdin.readline
from collections import deque

def main():
    def find_walls():
        walls = set()
        for i in range(I):
            for j in range(J):
                if mat[i][j]: continue
                walls.add((i, j))
        return walls

    def find_target():
        for i in range(I):
            for j in range(J):
                if mat[i][j]==2:
                    return i, j

    def BFS():
        ret = [[-1]*J for _ in range(I)]
        ti, tj = find_target()
        ret[ti][tj] = 0

        Q = deque([(ti, tj)])
        while Q:
            i, j = Q.popleft()
            for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
                si, sj = i+di, j+dj
                if not (0<=si<I and 0<=sj<J): continue
                if not ret[si][sj] == -1: continue
                if (si, sj) in walls: continue
                ret[si][sj] = ret[i][j]+1
                Q.append((si, sj))

        return ret

    def fill_walls():
        for wi, wj in walls:
            paths[wi][wj] = 0

    def SM(mat):
        for l in mat:
            print(*l)
        print()

    I, J = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(I)]
    walls = find_walls()
    paths = BFS()
    fill_walls()
    SM(paths)

main()