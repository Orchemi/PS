def main():
    N, M = map(int, input().split())
    cards = [sorted(list(map(int, input().split()))) for _ in range(N)]

    scores = [0]*N
    for m in range(M):
        cur_cards = [cards[i][m] for i in range(N)]
        cur_max = max(cur_cards)
        for i in range(N):
            if cur_cards[i] == cur_max:
                scores[i] += 1

    max_score = max(scores)
    ret = []
    for i in range(N):
        if scores[i] == max_score:
            ret.append(i+1)
    return ret

print(*main())