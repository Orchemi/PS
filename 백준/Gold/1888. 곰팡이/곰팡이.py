def main():
    def find_positions():
        positions = dict()
        for n in range(6):
            positions[n] = set()

        for i in range(I):
            for j in range(J):
                positions[mat[i][j]].add((i, j))

        positions.pop(0)
        nums = []
        for n in range(5, 0, -1):
            if positions[n]:
                nums.append(n)
            else:
                positions.pop(n)
        return nums, positions

    def get_all_values_set():
        all_values_set = set()
        for s in positions.values():
            all_values_set |= s
        return all_values_set

    def check_is_one():
        # 값이 있는 한 점 찾기
        all_values_set = get_all_values_set()
        fi, fj = all_values_set.pop()
        all_values_set.add((fi, fj))

        # 해당 좌표로부터 BFS
        visit = set()
        Q = {(fi, fj)}
        while Q:
            ni, nj = Q.pop()
            if (ni, nj) in visit: continue
            visit.add((ni, nj))
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                si, sj = ni+di, nj+dj
                if not (0<=si<I and 0<=sj<J): continue
                if not mat[si][sj]: continue
                if (si, sj) in visit: continue
                Q.add((si, sj))

        # visit과 all_values_set이 같으면 one group
        other_group = all_values_set-visit
        return False if other_group else True

    def expand():
        for n in nums:
            expand_set = set()
            for ni, nj in positions[n]:
                for di in range(-n, n+1):
                    si = ni+di
                    for dj in range(-n, n+1):
                        sj = nj+dj
                        if not (0<=si<I and 0<=sj<J): continue
                        if mat[si][sj] >= n: continue
                        expand_set.add((si, sj))
            for ei, ej in expand_set:
                mat[ei][ej] = n

            for m in nums:
                if m==n:
                    positions[m] |= expand_set
                else:
                    positions[m] -= expand_set

    I, J = map(int, input().split())
    mat = [list(map(int, input())) for _ in range(I)]
    nums, positions = find_positions()
    day = 0
    while True:
        if check_is_one(): return day
        expand()
        day += 1

print(main())