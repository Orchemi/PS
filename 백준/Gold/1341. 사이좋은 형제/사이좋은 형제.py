def make_mothers():
    global MAXX
    mothers = []
    n = 2
    while n < MAXX:
        mothers.append(n - 1)
        n *= 2
    return mothers


def make_ab(mothers):
    global MAXX
    a, m = map(int, input().split())
    for mother in mothers:
        if not mother%m:
            sq = mother//m
            aa = a*sq
            bb = mother - aa
            return aa, bb
    return 0

def is_odd(n):
    return n%2


def main():
    mothers = make_mothers()
    ret = make_ab(mothers)
    if not ret: return -1
    a, b = ret

    ans = ''
    while a or b:
        if a and is_odd(a):
            if is_odd(b): return -1
            ans = '*' + ans
            a-=1

        elif b and is_odd(b):
            if is_odd(a): return -1
            ans = '-' + ans
            b-=1

        else: return -1

        a, b = a//2, b//2

    return ans if len(ans) <= 60 else -1

MAXX = 2**65
print(main())