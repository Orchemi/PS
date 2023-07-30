def main():
    def check_end():
        if txt1[0]!=txt2[0]: return False
        if txt1[-1]!=txt2[-1]: return False
        return True

    def check_mu():
        mu = set('aeiou')
        rest1 = ''
        rest2 = ''
        for i in range(1, N-1):
            if not txt1[i] in mu:
                rest1 += txt1[i]
            if not txt2[i] in mu:
                rest2 += txt2[i]
        return rest1==rest2

    def check_all():
        D1 = {}
        for t in txt1:
            D1[t] = D1.get(t, 0) + 1

        D2 = {}
        for t in txt2:
            D2[t] = D2.get(t, 0) + 1

        return D1==D2

    N = int(input())
    txt1 = input()
    txt2 = input()
    if not check_end(): return 'NO'
    if not check_mu(): return 'NO'
    if not check_all(): return 'NO'
    return 'YES'

print(main())