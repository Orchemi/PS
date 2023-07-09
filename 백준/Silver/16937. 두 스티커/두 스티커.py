def main():
    def find_possible_form(sa, sb):
        i1, j1 = sa
        i2, j2 = sb
        for tryI, tryJ in ((i1+i2, max(j1,j2)),(i1+j2, max(j1,i2)),(max(i1,i2),j1+j2),(max(i1,j2),j1+i2)):
            for II, JJ in ((I, J), (J, I)):
                if tryI<=II and tryJ<=JJ: return i1*j1+i2*j2
        return 0

    I, J = map(int, input().split())
    N = int(input())
    stickers = [list(map(int, input().split())) for _ in range(N)]

    maxx = 0
    for i in range(N-1):
        sa = stickers[i]
        for j in range(i+1, N):
            sb = stickers[j]
            maxx = max(maxx, find_possible_form(sa, sb))
    return maxx

print(main())