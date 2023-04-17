import sys
input = sys.stdin.readline

def main():
    def find_largest_group():
        def find_group(i, j):
            v = mat[i][j]
            ret_set = set()
            cnt = 0
            move_set = set([(i, j)])
            while move_set:
                ni, nj = move_set.pop()
                if (ni, nj) in ret_set: continue
                ret_set.add((ni, nj))
                visit[ni][nj] = 1
                cnt += 1
                for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    si, sj = ni+di, nj+dj
                    if not (0<=si<N and 0<=sj<N): continue
                    if mat[si][sj] in {0, v}:
                        move_set.add((si, sj))

            return cnt, ret_set

        def find_suitable_group():
            gl = len(max_cnt_groups)
            rainbow_blocks = [0]*gl
            suitable_group_idx = 0

            # 무지개 블록 개수 구하기
            for i in range(gl):
                group = max_cnt_groups[i]
                for gi, gj in group:
                    if mat[gi][gj]: continue
                    rainbow_blocks[i] += 1

            # 최대 무지개 개수 가진 그룹 구하기
            max_rainbow_block_cnt = max(rainbow_blocks)
            max_rainbow_group_idxs = []
            for i in range(gl):
                if rainbow_blocks[i] == max_rainbow_block_cnt:
                    max_rainbow_group_idxs.append(i)
            if len(max_rainbow_group_idxs)==1:
                return max_cnt_groups[max_rainbow_group_idxs[0]]

            # 이 그룹들의 기준 블록 구하기
            ret_group_idx = 0
            ret_std_ij = [-1, -1]
            for i in max_rainbow_group_idxs:
                group = max_cnt_groups[i]
                cur_std_ij = [201, 201]
                for gi, gj in group:
                    if not mat[gi][gj]: continue
                    if cur_std_ij[0] > gi:
                        cur_std_ij = [gi, gj]
                    elif cur_std_ij[0]==gi:
                        cur_std_ij = [gi, min(cur_std_ij[1], gj)]

                # 현재 그룹의 기준 블럭이 전체 그룹의 기준 블럭보다 우선순위 상위인지
                if ret_std_ij[0] < cur_std_ij[0]:
                    ret_group_idx = i
                    ret_std_ij = cur_std_ij
                elif ret_std_ij[0] == cur_std_ij[0]:
                    if ret_std_ij[1] < cur_std_ij[1]:
                        ret_group_idx = i
                        ret_std_ij = cur_std_ij

            return max_cnt_groups[ret_group_idx]


        visit = [[0]*N for _ in range(N)]
        max_cnt, max_cnt_groups = 0, [set()]
        for i in range(N):
            for j in range(N):
                if mat[i][j] in {0, -1, -2}: continue
                if visit[i][j]: continue
                cur_cnt, cur_cnt_group = find_group(i, j)
                if max_cnt < cur_cnt:
                    max_cnt = cur_cnt
                    max_cnt_groups = [cur_cnt_group]
                elif max_cnt==cur_cnt:
                    max_cnt_groups.append(cur_cnt_group)

        if max_cnt==1 or len(max_cnt_groups)==1:
            return max_cnt, max_cnt_groups[0]
        else:
            return max_cnt, find_suitable_group()

    def remove_largest_group():
        for i, j in max_cnt_group:
            mat[i][j] = -2

    def gravity():
        new_mat = [[-2]*N for _ in range(N)]
        for j in range(N):
            idx = 0
            lst = []
            while idx < N:
                if mat[idx][j]==-1:
                    new_mat[idx][j]=-1
                    bottom = idx-1
                    while lst:
                        new_mat[bottom][j] = lst.pop()
                        bottom -= 1
                else:
                    if mat[idx][j]==-2:
                        idx += 1
                        continue
                    lst.append(mat[idx][j])
                idx += 1

            if lst:
                bottom = N-1
                while lst:
                    new_mat[bottom][j] = lst.pop()
                    bottom -= 1
        return new_mat

    def rotate():
        new_mat = []
        for j in range(N-1, -1, -1):
            new_mat.append([mat[i][j] for i in range(N)])
        return new_mat


    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    ret = 0
    while True:
        max_cnt, max_cnt_group = find_largest_group()
        if max_cnt<=1: return ret
        ret += max_cnt**2
        remove_largest_group()
        mat = gravity()
        mat = rotate()
        mat = gravity()

print(main())