def main():
    def make_vals():
        vals = [0]*32
        for i in range(21):
            vals[i] = 2*i
        vals[21], vals[22], vals[23] = 13, 16, 19
        vals[24], vals[25] = 22, 24
        vals[26], vals[27], vals[28] = 28, 27, 26
        vals[29], vals[30], vals[31] = 25, 30, 35
        return vals

    def make_children():
        children = {}
        for n in range(20):
            children[n] = n+1
        for a, b in ((21, 23), (24, 25), (26, 28), (29, 31)):
            for n in range(a, b):
                children[n] = n+1
        children[23] = children[25] = children[28] = 29
        children[31] = 20
        children[20] = -1

        special_children = {5: 21, 10: 24, 15: 26}
        return children, special_children

    def move(move_cnt, acc, pos_list, pos_set):
        def move_next(is_special, cur_max_acc):
            ret = cur_max_acc
            step_cnt = 1
            cur_pos = special_children[p] if is_special else children[p]
            if cur_pos != -1:
                while step_cnt < cur_move:
                    cur_pos = children[cur_pos]
                    if cur_pos==-1: break
                    step_cnt += 1

            new_pos_list = pos_list[:]
            new_pos_list[pi] = cur_pos
            new_pos_set = pos_set - {p}
            if cur_pos==-1:
                new_pos_list.pop(pi)
                ret = max(ret, move(move_cnt+1, acc, new_pos_list, new_pos_set))
            else:
                if cur_pos in pos_set: return 0
                ret = max(ret, move(move_cnt+1, acc+vals[cur_pos], new_pos_list, new_pos_set|{cur_pos}))
            return ret

        if move_cnt==10: return acc

        cur_max_acc = acc
        cur_move = moves[move_cnt]
        for pi in range(len(pos_list)):
            p = pos_list[pi]
            is_special = p in special_children_set
            cur_max_acc = max(cur_max_acc, move_next(is_special, cur_max_acc))
        return cur_max_acc


    moves = list(map(int, input().split()))
    vals = make_vals()
    children, special_children = make_children()
    special_children_set = {5, 10, 15}
    return move(0, 0, [0, 0, 0, 0], {0})

print(main())