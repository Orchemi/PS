def main():
    N, new_score, P = map(int, input().split())
    if not N: return 1 if P else -1

    scores = list(map(int, input().split()))
    rank = 1
    for score in scores:
        if score > new_score:
            rank += 1
        else: break

    same_cnt = scores.count(new_score)
    return rank if rank+same_cnt <= P else -1

print(main())