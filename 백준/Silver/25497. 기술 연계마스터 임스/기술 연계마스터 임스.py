def main():
    N = int(input())
    txt = input()
    cnt = 0
    IS = {'L', 'R', 'S', 'K'}
    PR = {'L', 'S'}
    PT = {'R': 'L', 'K': 'S'}
    D = {}
    for i in txt:
        if i not in IS:
            cnt += 1
        elif i in PR:
            D[i] = D.get(i, 0) + 1
        else:
            if not D.get(PT[i], 0): break
            D[PT[i]] -= 1
            cnt += 1

    return cnt

print(main())