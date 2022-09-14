import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def calc_time(n):
    global build_first, times, is_built

    if is_built[n] != -1:
        return is_built[n]

    if not build_first[n]:
        return times[n]

    max_time = 0
    for first in build_first[n]:
        ret = calc_time(first)
        if max_time < ret:
            max_time = ret

    is_built[n] = max_time + times[n]
    return is_built[n]


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    times = [0]+list(map(int, input().split()))
    build_first = [[] for _ in range(N + 1)]
    is_built = [-1]*(N+1)

    for _ in range(K):
        a, b = map(int, input().split())
        build_first[b].append(a)

    W = int(input())
    print(calc_time(W))