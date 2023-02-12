import sys
input = sys.stdin.readline

def main():
    def find_left_hand():
        for j in range(N):
            for i in range(N):
                if mat[i][j]=='*': return i, j

    def find_heart(i, j):
        while True:
            if mat[i-1][j]=='*': return i, j
            j += 1

    def calc_length(i, j, di, dj):
        l = 0
        while True:
            if not (0<=i+di<N and 0<=j+dj<N): return l
            if not mat[i+di][j+dj]=='*': return l
            l += 1
            i += di
            j += dj


    N = int(input())
    mat = [list(input()) for _ in range(N)]
    bi, bj = find_left_hand()
    hi, hj = find_heart(bi, bj)
    print(hi+1, hj+1)

    lengths = []
    lengths.append(calc_length(hi, hj, 0, -1))
    lengths.append(calc_length(hi, hj, 0, 1))
    lengths.append(calc_length(hi, hj, 1, 0))

    wi, wj = hi+lengths[2], hj
    lengths.append(calc_length(wi, wj-1, 1, 0))
    lengths.append(calc_length(wi, wj+1, 1, 0))
    print(*lengths)

main()