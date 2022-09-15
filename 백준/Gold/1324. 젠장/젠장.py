N = int(input())
day1 = [0]+list(map(int, input().split()))
day2 = [0]+list(map(int, input().split()))
set_day2 = set(day2)
ret = [set() for _ in range(N+1)]
ret[0].add((0, 0))

for i in range(1, N+1):
    ret[i] = ret[i-1]
    cur_v = day1[i]
    # print(i)
    if cur_v not in set_day2: continue

    add_list = set()
    for tupp in ret[i]:
        mi, ms = tupp
        if day2[mi] >= cur_v: continue

        for ii in range(mi+1, N+1):
            if day2[ii] != cur_v: continue

            add_list.add((ii, ms + 1))

    check_obj = {}
    for k, v in add_list:
        ov = check_obj.get(k)
        if ov and ov >= v: continue
        check_obj[k] = v

    for k, v in check_obj.items():
        ret[i].add((k, v))

    if not i%10:
        clean = dict()
        for idx, cnt in ret[i]:
            if clean.get(cnt, []):
                clean[cnt].append([idx, day2[idx]])
            else:
                clean[cnt] = [[idx, day2[idx]]]

        max_cnt = max(clean.keys())
        tmp = set()
        for cnt, arrs in clean.items():
            if (N - i) + cnt < max_cnt: continue
            arrs.sort(key=lambda x: (x[1], x[0]))

            cur_val = -1
            for idx, val in arrs:
                if val == cur_val: continue
                cur_val = val
                tmp.add((idx, cnt))

        ret[i] = tmp

ans = 0
for sett in ret[N]:
    if ans < sett[1]:
        ans = sett[1]

print(ans)