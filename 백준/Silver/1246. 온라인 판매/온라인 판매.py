def main():
    N, M = map(int, input().split())
    buyers = sorted([int(input()) for _ in range(M)])
    costs = sorted(list(set(buyers)))
    max_benefit = 0
    max_cost = 0
    for m in range(M):
        cur_count = M-m if M-m <= N else N
        cur_benefit = buyers[m]*cur_count
        if max_benefit < cur_benefit:
            max_benefit = cur_benefit
            max_cost = buyers[m]
    return [max_cost, max_benefit]

print(*main())