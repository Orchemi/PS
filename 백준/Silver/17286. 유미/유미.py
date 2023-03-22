def calc_len(i1, i2):
    x1, y1 = positions[i1]
    x2, y2 = positions[i2]
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

def dfs(ni, visit, acc):
    global min_len
    if visit==[0, 1, 1, 1]:
        min_len = min(min_len, acc)

    for j in range(4):
        if visit[j]: continue
        new_visit = visit[:]
        new_visit[j] = 1
        dfs(j, new_visit, acc+calc_len(ni, j))

positions = [list(map(int, input().split())) for _ in range(4)]
min_len = 1e5
for ni in range(1, 4):
    visit = [0]*4
    visit[ni] = 1
    dfs(ni, visit, calc_len(0, ni))
print(int(min_len))