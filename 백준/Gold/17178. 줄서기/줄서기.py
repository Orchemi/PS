def main():
    def find_lines():
        lines = [[]]
        lines_set = [set()]
        for i in range(N):
            _line = [t.split('-') for t in input().split()]
            line = [(ord(_a)-64)*1000 + int(_n) for _a, _n in _line][::-1]
            lines.append(line)
            lines_set.append(set(line))

        return lines, lines_set


    def find_total_order():
        total_order = []
        for line in lines:
            total_order += line
        return sorted(total_order)


    def find_pos_idx(t):
        for i in range(N+1):
            if t in lines_set[i]: return i


    def process_one(t):
        pi = find_pos_idx(t)
        if pi==0:
            if lines[pi][-1]!=t: return 'BAD'
            lines[pi].pop()
            lines_set[pi].remove(t)
            return 0
        else:
            while lines[pi][-1]!=t:
                pv = lines[pi].pop()
                lines[0].append(pv)
                lines_set[0].add(pv)

            lines[pi].pop()
            lines_set[pi].remove(t)
            return pi


    N = int(input())
    lines, lines_set = find_lines()
    total_order = find_total_order()
    for t in total_order:
        remove_idx = process_one(t)
        if remove_idx == 'BAD': return 'BAD'
        if remove_idx > 0 and not lines[remove_idx]:
            lines.pop(remove_idx)
            lines_set.pop(remove_idx)
            N -= 1

    return 'GOOD' if lines==[[]] else 'BAD'

print(main())