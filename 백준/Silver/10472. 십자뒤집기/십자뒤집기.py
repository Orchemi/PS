import sys
input = sys.stdin.readline
from collections import deque

def main():
    def make_mat():
        tmp = [list(input()) for _ in range(3)]
        mat = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                if tmp[i][j]=='*':
                    mat[i][j] = 1
        return mat

    def bfs():
        Q = deque()
        Q.append([[0]*3 for _ in range(3)])
        while Q:
            tmp = Q.popleft()
            tmp_key = convert_str(tmp)
            for i in range(3):
                for j in range(3):
                    copied_tmp = deep_copy(tmp)
                    for di, dj in ((0,0),(-1,0),(1,0),(0,-1),(0,1)):
                        si, sj = i+di, j+dj
                        if not (0<=si<3 and 0<=sj<3): continue
                        copied_tmp[si][sj] ^= 1
                    copied_tmp_key = convert_str(copied_tmp)
                    if copied_tmp_key == ans:
                        return D[tmp_key]
                    if D.get(copied_tmp_key, 0): continue
                    D[copied_tmp_key] = D[tmp_key]+1
                    Q.append(copied_tmp)

    def deep_copy(mat):
        return [l[:] for l in mat]

    def convert_str(mat):
        ret = ''
        for i in range(3):
            for j in range(3):
                ret += str(mat[i][j])
        return ret

    D = {'000000000': 1}
    mat = make_mat()
    ans = convert_str(mat)
    if D.get(ans, 0): return 0
    return bfs()


T = int(input())
for _ in range(T):
    print(main())