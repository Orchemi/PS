from itertools import combinations

def foo(team):
    ssum = 0
    for i in team:
        for j in team:
            ssum += mat[i][j]
            ssum += mat[j][i]
    return ssum//2

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
minDiff = 0xfffff
for comb in combinations(range(N), N//2):
    teamA = set(comb)
    teamB = set(range(N)) - teamA
    minDiff = min(minDiff, abs(foo(teamA) - foo(teamB)))

print(minDiff)