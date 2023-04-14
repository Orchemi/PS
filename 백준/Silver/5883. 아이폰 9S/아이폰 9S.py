def main():
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    maxx = 0

    removed = set()
    for a in arr:
        if a in removed: continue
        removed.add(a)
        cur_max = 0
        cur_len = 0
        cur_val = -1
        for b in arr:
            if b==a: continue
            if cur_val==b:
                cur_len+=1
            else:
                cur_max = max(cur_max, cur_len)
                cur_len = 1
                cur_val = b
        maxx = max(maxx, cur_max, cur_len)
    return maxx

print(main())