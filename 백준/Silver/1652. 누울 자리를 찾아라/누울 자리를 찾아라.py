def main():
    def calc_line(lst):
        i = 0
        tmp = 0
        while i < N-1:
            if lst[i]=='X':
                i += 1
                continue
            if lst[i+1]=='.':
                tmp += 1
                while i < N and lst[i]=='.':
                    i += 1
            else:
                i += 1
        return tmp

    N = int(input())
    mat = [list(input()) for _ in range(N)]

    v_ret = 0
    for lst in mat:
        v_ret += calc_line(lst[:])

    h_ret = 0
    for j in range(N):
        lst = []
        for i in range(N):
            lst.append(mat[i][j])
        h_ret += calc_line(lst)

    return v_ret, h_ret

print(*main())