def dfs(i):
    if i == 5:
        global scoreMax
        scoreNow = check()
        scoreMax = max(scoreMax, scoreNow)
        return

    for k in range(5):
        if visited[k]: continue
        visited[k] = 1
        stack.append(arr[k])
        dfs(i+1)
        visited[k] = 0
        stack.pop()

def check():
    global stack
    # 변수 설정
    # RSF = SF = F = FH = FC = 0
    # TRI = TP = OP = 0
    cs = [i[0] for i in stack]
    ns = [i[1] for i in stack]
    nd = {}
    for n in ns:
        nd[n] = nd.get(n, 0) + 1
    ndKeys = nd.keys()
    ndVals = sorted(nd.values())
    mn = max(ns)

    # color5 확인
    color5 = 1
    stdC = stack[0][0]
    for i in range(1, 5):
        if stdC != stack[i][0]:
            color5 = 0
            break

    # run5 확인
    run5 = 1
    stdN = stack[0][1]
    for i in range(1, 5):
        if stdN + i != stack[i][1]:
            run5 = 0
            break

    # RSF 확인
    if color5 == run5 == 1:
        return mn + 900

    # FC, FH 확인
    if len(nd)==2:
        k1, k2 = ndKeys
        n1, n2 = nd[k1], nd[k2]
        # FC인 경우
        if n1==4:
            return k1+800
        elif n1==1:
            return k2+800
        # FH인 경우
        elif n1==3:
            return k1*10 + k2 + 700
        else:
            return k2*10 + k1 + 700

    # F, S 확인
    if color5: return mn + 600
    if run5: return ns[-1] + 500

    # TRI 확인
    if 3 in ndVals:
        for k in ndKeys:
            if nd[k] == 3:
                return k + 400

    # TP 확인
    if ndVals == [1, 2, 2]:
        tmp = []
        for k in ndKeys:
            if nd[k] == 2:
                tmp.append(k)
        k1, k2 = sorted(tmp)
        return k2*10 + k1 + 300

    # OP 확인
    if len(nd) == 4:
        for k in ndKeys:
            if nd[k] == 2:
                return k + 200

    return mn + 100


arr = []
for _ in range(5):
    a = input().split()
    arr.append((a[0], int(a[1])))

stack = []
visited = [0]*5
scoreMax = 0
dfs(0)
print(scoreMax)