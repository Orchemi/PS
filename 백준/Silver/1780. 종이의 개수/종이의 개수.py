import sys
input = sys.stdin.readline

def main(ni, nj, nl):
    nv = mat[ni][nj]
    for i in range(ni, ni+nl):
        for j in range(nj, nj+nl):
            if not mat[i][j]==nv:
                divide(ni, nj, nl)
                return

    global cnt
    cnt[nv+1] += 1
    return


def divide(ni, nj, nl):
    tl = nl//3
    for i in range(ni, ni+nl, tl):
        for j in range(nj, nj+nl, tl):
            main(i, j, tl)
    return


N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
cnt = [0]*3
main(0, 0, N)
print(*cnt, sep='\n')