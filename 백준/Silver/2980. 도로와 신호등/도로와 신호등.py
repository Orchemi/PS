N, L = map(int, input().split())
traffics = {}
for _ in range(N):
    D, R, G = map(int, input().split())
    traffics[D] = (R, G)

P = sorted(traffics.keys())
S = set(P)

time = 0
cur_pos = 0
while cur_pos < L:
    if not cur_pos in S:
        time += 1
        cur_pos += 1
        continue

    R, G = traffics[cur_pos]
    M = R+G
    rest = time%M
    if not rest:
        time += R+1
        cur_pos += 1
    else:
        if rest < R:
            time += R-rest+1
            cur_pos += 1
        else:
            time += 1
            cur_pos += 1

print(time)