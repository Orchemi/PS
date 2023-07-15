import sys
sys.setrecursionlimit(1000000)

def main():
    def draw_tree():
        p = [0]*(N+1)
        for _ in range(N-1):
            pn, cn = map(int, input().split())
            p[cn] = pn
        return p

    def find_ps(cn):
        return [cn] + find_ps(p[cn]) if p[cn] else [cn]

    def rearrange_ps():
        psa, psb = find_ps(a), find_ps(b)
        la, lb = len(psa), len(psb)
        if la > lb:
            psa = psa[la-lb:]
        else:
            psb = psb[lb-la:]
        return psa, psb, min(la, lb)

    N = int(input())
    p = draw_tree()
    a, b = map(int, input().split())
    psa, psb, L = rearrange_ps()
    for i in range(L):
        if psa[i] == psb[i]: return psa[i]


T = int(input())
for _ in range(T):
    print(main())