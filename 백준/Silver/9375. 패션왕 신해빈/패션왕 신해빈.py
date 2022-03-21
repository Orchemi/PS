import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 분류 key, 같은 분류 옷 리스트를 value로 하는 딕셔너리
    dictC = {}
    N = int(input())
    for _ in range(N):
        c, p = input().split()
        dictC[p] = dictC.get(p, []) + [c]

    # 각 분류마다 개수를 구해 1을 더해 lenlst에 저장
    lenlst = []
    karr = dictC.keys()
    for k in karr:
        lst = dictC[k]
        lenlst.append(len(lst)+1)

    # 이를 모두 곱함
    ret = 1
    for l in lenlst:
        ret *= l

    # ret에서 1을 빼서 출력(모두 없는 경우)
    print(ret-1)