def main():
    def check_per_line(line):
        cnt = 0
        sold_out = [j for j in range(J) if line[j]]
        sold_out.append(J)
        l = len(sold_out)

        prev = -1
        for i in range(l):
            blank_line_count = sold_out[i]-prev-1
            cnt += max(0, blank_line_count-K+1)
            prev = sold_out[i]
        return cnt


    I, J, K = map(int, input().split())
    mat = [list(map(int, input())) for _ in range(I)]
    ret = 0
    for i in range(I):
        ret += check_per_line(mat[i])
    return ret

print(main())