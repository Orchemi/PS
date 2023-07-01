def main():
    N, L = map(int, input().split())
    holes = sorted([list(map(int, input().split())) for _ in range(N)])

    safe = 0
    cnt = 0
    for hs, he in holes:
        if he <= safe: continue
        safe = max(safe, hs)
        cur_hole_len = he-safe
        need_cnt = cur_hole_len//L
        if cur_hole_len%L:
            need_cnt += 1
        cnt += need_cnt
        safe += need_cnt*L
    return cnt

print(main())