import sys
from itertools import combinations

def main():
    def calc_min_single():
        return min(arr)

    def calc_min_double():
        S = {comb for comb in combinations(range(6), 2)}
        del_S = {(0, 5), (1, 4), (2, 3)}
        minn = 1000
        for a, b in S - del_S:
            minn = min(minn, arr[a]+arr[b])
        return minn

    def calc_min_triple():
        S = {(0,1,2),(0,1,3),(0,4,2),(0,4,3), (5,1,2),(5,1,3),(5,4,2),(5,4,3)}
        minn = 1000
        for a, b, c in S:
            minn = min(minn, arr[a]+arr[b]+arr[c])
        return minn

    def check_outer():
        min_single = calc_min_single()
        min_double = calc_min_double()
        min_triple = calc_min_triple()

        sq_triple = 4
        sq_double = 4*(N-2)+4*(N-1) if N > 1 else 4
        sq_single = 4*(N-1)*(N-2)+(N-2)**2 if N > 1 else 0

        single = min_single * sq_single
        double = min_double * sq_double
        triple = min_triple * sq_triple
        return single + double + triple


    N = int(input())
    arr = list(map(int, input().split()))
    if N==1: return sum(arr)-max(arr)
    return check_outer()

print(main())