def main():
    def find_possible_As():
        M = min(L, 3)
        possible_As = []
        for e in range(1, M+1):
            possible_As.append(txt[:e])
        return possible_As

    def is_possible(A):
        cur_num = int(A)
        next_num = cur_num+1
        tl = len(str(next_num))
        i = len(str(cur_num))

        while i < L:
            if i+tl > L: return False
            find_num = int(txt[i:i+tl])
            if next_num != find_num: return False
            cur_num += 1
            next_num += 1
            i += tl
            tl = len(str(next_num))
        return cur_num

    txt = input()
    L = len(txt)
    possible_As = find_possible_As()
    for A in possible_As:
        ret = is_possible(A)
        if ret: return [A, ret]

print(*main())