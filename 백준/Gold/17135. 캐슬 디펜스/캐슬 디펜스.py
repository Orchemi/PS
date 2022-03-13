import sys
input = sys.stdin.readline

def archor(i, s):
    global archors, used, W, D, H, Hdec

    if i==3:
        War(archors)
        Hdec = H
        return

    for k in range(s, W):
        if not used[k]:
            used[k] = 1
            archors.append(k)
            archor(i+1, k+1)
            used[k] = 0
            archors.pop()


def War(archors):
    global mat, Hdec, matdec, max_kill
    matdec = []
    for lst in mat:
        matdec.append(lst[::])

    sum_kill = 0
    while Hdec > 0:
        setArchors(archors)
        sum_kill += attack(archors)
        matdec.pop()
        matdec.pop()
        Hdec -= 1

    max_kill = max(max_kill, sum_kill)

def setArchors(archors):
    global W, matdec

    lst = [2]*W
    for archor in archors:
        lst[archor] = 3
    matdec.append(lst)

def attack(archors):
    global matdec
    global D
    attack_lst = []

    for archor in archors:
        attackXY = selectEnemy(archor, D)
        if not attackXY:
            continue
        
        if not attackXY in attack_lst:
            attack_lst.append(attackXY)

    attackCnt = 0
    for attack in attack_lst:
        ai, aj = attack
        matdec[ai][aj] = 0
        attackCnt += 1

    return attackCnt


def selectEnemy(archor, D):
    global Hdec, W
    areaQ = [(Hdec, archor, 0)]
    start = -1
    end = 1
    visited = [[0]*W for _ in range(Hdec+1)]

    while start < end-1:
        start += 1
        ni, nj, dis = areaQ[start]

        if dis == D:
            if matdec[ni][nj]==1:
                return ni, nj
            else:
                continue

        didj = [(0,-1), (-1,0), (0,1)]
        for di, dj in didj:
            if 0<=ni+di and 0<=nj+dj<W:
                if matdec[ni+di][nj+dj]==1 and dis<=D:
                    return ni+di, nj+dj

                if not visited[ni+di][nj+dj] and dis<D:
                    visited[ni+di][nj+dj] = 1
                    areaQ.append((ni+di, nj+dj, dis+1))
                    end += 1

H, W, D = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(H)]
Hdec = H
matdec = []

archors = []
used = [0]*W
enemies = []
max_kill = 0
archor(0, 0)

print(max_kill)