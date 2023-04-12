def main():
    def find_next_min_val():
        next_move = []
        for i in range(3):
            if idxs[i]!=lens[i]:
                next_move.append(nums[i][idxs[i]])
        return sorted(next_move)[0]

    def find_next_move_idx():
        for i in range(3):
            if idxs[i] >= lens[i]: continue
            if nums[i][idxs[i]] == next_min_val: return i

    lens = list(map(lambda x: int(x)-1, input().split()))
    nums = [sorted(list(map(int, input().split()))) for _ in range(3)]
    idxs = [0]*3

    ret = 1e10
    while [idxs[0], idxs[1], idxs[2]] != lens:
        cur_nums = [nums[i][idxs[i]] for i in range(3)]
        ret = min(ret, max(*cur_nums)-min(*cur_nums))

        next_min_val = find_next_min_val()
        next_move_idx = find_next_move_idx()
        idxs[next_move_idx] += 1

    return ret

print(main())