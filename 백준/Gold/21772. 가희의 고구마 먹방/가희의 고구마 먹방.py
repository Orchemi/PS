def main():
    def find_G():
        for i in range(I):
            for j in range(J):
                if mat[i][j] == 'G':
                    return i, j

    def dfs(i, j, move, cnt, ate):
        if move == T:
            return cnt

        cur_max = 0
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            si, sj = i + di, j + dj
            if not (0 <= si < I and 0 <= sj < J): continue
            if mat[si][sj] == '#': continue

            new_ate = set([*ate])
            new_cnt = cnt
            if mat[si][sj] == 'S':
                if not (si, sj) in ate:
                    new_ate.add((si, sj))
                    new_cnt += 1
                dfs_max = dfs(si, sj, move + 1, new_cnt, new_ate)
            else:
                dfs_max = dfs(si, sj, move + 1, cnt, new_ate)
            cur_max = max(cur_max, dfs_max)

        return cur_max

    I, J, T = map(int, input().split())
    mat = [list(input()) for _ in range(I)]
    gi, gj = find_G()
    ret = dfs(gi, gj, 0, 0, set())
    return ret

print(main())