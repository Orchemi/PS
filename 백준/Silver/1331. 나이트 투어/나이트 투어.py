def main():
    def reform(p):
        a, b = list(p)
        i, j = ord(a)-64, int(b)
        return i, j

    def calc_dis(i1, j1, i2, j2):
        mi, mj = abs(i1-i2), abs(j1-j2)
        return sorted([mi, mj]) == [1, 2]

    moves = [input() for _ in range(36)]
    if len(moves) != len(set(moves)): return 'Invalid'

    bi, bj = reform(moves.pop())
    ni, nj = bi, bj
    for m in moves:
        si, sj = reform(m)
        if not calc_dis(ni, nj, si, sj): return 'Invalid'
        ni, nj = si, sj

    return 'Valid' if calc_dis(ni, nj, bi, bj) else 'Invalid'

print(main())