import sys
input = sys.stdin.readline

def main():
    def check_ices():
        ices = set()
        for i in range(I):
            for j in range(J):
                if mat[i][j]:
                    ices.add((i, j))
        return ices

    def check_is_one():
        ii, ij = ices.pop()
        ices.add((ii, ij))
        linked_ices = check_linked(ii, ij)
        return linked_ices == ices

    def check_linked(ii, ij):
        linked_ices = set()
        Q = set()
        Q.add((ii, ij))
        while Q:
            ii, ij = Q.pop()
            if (ii, ij) in linked_ices: continue
            linked_ices.add((ii, ij))
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                si, sj = ii+di, ij+dj
                if not (0<=si<I and 0<=sj<J): continue
                if not mat[si][sj]: continue
                Q.add((si, sj))
        return linked_ices

    def melt():
        target_ices = []
        for ii, ij in ices:
            melt_cnt = melt_one(ii, ij)
            target_ices.append((ii, ij, melt_cnt))

        remove_ices = set()
        for ii, ij, mcnt in target_ices:
            mat[ii][ij] -= mcnt
            if mat[ii][ij]: continue
            remove_ices.add((ii, ij))
        return remove_ices

    def melt_one(i, j):
        cnt = 0
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            si, sj = i+di, j+dj
            if not (0<=si<I and 0<=sj<J): continue
            if mat[si][sj]: continue
            cnt += 1
        return cnt if mat[i][j] > cnt else mat[i][j]


    I, J = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(I)]
    ices = check_ices()
    if not ices: return 0

    year = 0
    while True:
        if not check_is_one(): return year
        year += 1
        ices -= melt()
        if not ices: return 0

print(main())