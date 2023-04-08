from collections import deque
from itertools import permutations

def main():
    def make_damages():
        damages = [9, 3, 1]
        D = [[] for _ in range(4)]
        for n in range(1, 4):
            D[n] = [lst for lst in permutations(damages[:n], n)]
        return D

    N = int(input())
    scvs = sorted(list(map(int, input().split())))
    Q = deque([(scvs, N, 0)])
    damages = make_damages()

    watched = set()
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
            Q.append((attacked_scvs, scvs_cnt-kill_cnt, attack_cnt+1))

print(main())