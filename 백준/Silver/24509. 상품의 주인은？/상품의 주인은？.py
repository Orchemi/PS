import sys
input = sys.stdin.readline

def main():
    def find_winner(D):
        scores = sorted(D.keys(), reverse=True)
        for j in range(len(scores)):
            maxs = sorted(D[scores[j]])
            for m in maxs:
                if not m in ret:
                    return m

    N = int(input())
    F = [dict() for _ in range(4)]
    for _ in range(N):
        X, *scores = map(int, input().split())
        for i in range(4):
            if not F[i].get(scores[i], []):
                F[i][scores[i]] = []
            F[i][scores[i]].append(X)

    ret = []
    for i in range(4):
        ret.append(find_winner(F[i]))
    return ret

print(*main())