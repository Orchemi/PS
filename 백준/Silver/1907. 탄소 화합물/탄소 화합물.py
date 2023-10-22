def main():
    def find_composition(txt):
        def count_atom(c):
            ret = 0
            i = 0
            while i < tl:
                if not txt[i] == c:
                    i += 1
                    continue

                count = ''
                while True:
                    if i+1 == tl: break
                    if not txt[i+1].isnumeric(): break
                    count += txt[i+1]
                    i += 1

                ret += int(count) if count else 1
                i += 1
            return ret

        tl = len(txt)
        return [count_atom(c) for c in 'CHO']


    left, right = input().split('=')
    mol1, mol2 = left.split('+')

    def brute_force():
        def compare(m): return l1[m]*i + l2[m]*j == r[m]*k
        l1, l2 = find_composition(mol1), find_composition(mol2)
        r = find_composition(right)
        for i in range(1, 11):
            for j in range(1, 11):
                for k in range(1, 11):
                    flag = True
                    for m in range(3):
                        if not compare(m):
                            flag = False
                            break
                    if flag: return i, j, k

    return brute_force()

print(*main())