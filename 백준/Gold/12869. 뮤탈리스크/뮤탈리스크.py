from collections import deque

def main():
    N = int(input())
    scvs = sorted(list(map(int, input().split())))
    Q = deque([(scvs, N, 0)])
    watched = set()
    damages = [
        [],
        [[9]],
        [[9,3], [3,9]],
        [[9,3,1],[9,1,3],[3,9,1],[3,1,9],[1,9,3],[1,3,9]]
    ]

    while Q:
        cur_scvs, scvs_cnt, attack_cnt = Q.popleft()
        if str(cur_scvs) in watched: continue
        watched.add(str(cur_scvs))

        for damage in damages[scvs_cnt]:
            attacked_scvs = []
            kill_cnt = 0
            for n in range(scvs_cnt):
                attacked_scv = cur_scvs[n] - damage[n]
                if attacked_scv <= 0:
                    kill_cnt += 1
                else:
                    attacked_scvs.append(attacked_scv)
            if kill_cnt == scvs_cnt: return attack_cnt+1
            Q.append((sorted(attacked_scvs), scvs_cnt-kill_cnt, attack_cnt+1))

print(main())