import sys; input = sys.stdin.readline

def calc(pos):
    global visited_pos, visited_per
    global pools, max_score, total

    if pos==11:
        if sum(visited_pos)==11 and max_score < total:
            max_score = total
        return

    # 해당 포지션을 담당할 사람이 있다면 다음 포지션
    if visited_pos[pos]:
        calc(pos+1)

    else:
        pool = pools[pos]
        for per, score in pool:
            if not visited_per[per]:
                visited_per[per] = 1
                visited_pos[pos] = 1
                total += score
                calc(pos+1)
                visited_per[per] = 0
                visited_pos[pos] = 0
                total -= score



T = int(input())
for _ in range(T):

    # mat 정의
    mat = [list(map(int, input().split())) for _ in range(11)]

    # pools 정의
    pools = [[] for _ in range(11)]
    for per, lst in enumerate(mat):
        for pos, score in enumerate(lst):
            if score:
                pools[pos].append((per, score))

    # 해당 포지션 가능한 유일한 사람 찾아 채우기
    visited_pos = [0]*11
    visited_per = [0]*11
    total = 0
    max_score = 0
    for pos in range(11):
        if len(pools[pos]) == 1:
            per, score = pools[pos][0]
            visited_per[per] = 1
            visited_pos[pos] = 1
            total += score

    calc(0)
    print(max_score)