N, L = map(int, input().split())
traffics = {}
for _ in range(N):
    D, R, G = map(int, input().split())
    traffics[D] = (R, G)
S = set(traffics.keys())

time = 0
cur_pos = 0
while cur_pos < L:
    if not cur_pos in S:
        time += 1
        cur_pos += 1
        continue

    R, G = traffics[cur_pos]
    rest = time % (R+G)
    acc = R-rest if rest<R else 0
    time += acc+1
    cur_pos += 1

print(time)