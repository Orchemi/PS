def divSection(depth, s, M):
    global groupA, groupB
    if depth == M:
        groupB = list(set(range(N)) - set(groupA))
        if checkLink(groupA) and checkLink(groupB):
            calcMin(groupA, groupB)


    for k in range(s, N):
        if not visited[k]:
            visited[k] = 1
            groupA.append(k)
            divSection(depth+1, k+1, M)
            visited[k] = 0
            groupA.pop()


def checkLink(group):
    global links

    if len(group) == 1:
        return True

    i = group[0]
    linkQ = []
    for s in links[i]:
        if s in group:
            linkQ.append([i, s])
    start = -1
    end = len(linkQ)
    visitedQ = [0]*N
    visitedQ[i] = 1
    while start < end-1:
        start += 1
        s1, s2 = linkQ[start]
        if not visitedQ[s2]:
            visitedQ[s2] = 1
            for s in links[s2]:
                if s in group:
                    linkQ.append([s2, s])
                    end += 1

    for s in group:
        if not visitedQ[s]:
            return False
    return True



def calcMin(groupA, groupB):
    global populations, ans

    sumA = 0
    for s in groupA:
        sumA += populations[s]

    sumB = 0
    for s in groupB:
        sumB += populations[s]

    diff = abs(sumA - sumB)
    if ans > diff:
        ans = diff


N = int(input())
populations = list(map(int, input().split()))
links = []
for k in range(N):
    n, *link = list(map(int, input().split()))
    link = [i-1 for i in link]
    links.append(link)

visited=[0]*N
groupA = []
ans = 1000
for M in range(1, N//2+1):
    divSection(0, 0, M)

ans = -1 if ans==1000 else ans
print(ans)