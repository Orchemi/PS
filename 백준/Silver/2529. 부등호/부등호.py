def dfs(i):
    global stack
    if i==N+1:
        if not check(stack[-2], ops[-1], stack[-1]): return
        global ansLst
        txt = ''.join(list(map(str, stack)))
        ansLst.append(txt)
        return

    if i > 1:
        if not check(stack[i-2], ops[i-2], stack[i-1]):
            return

    for k in range(10):
        if visited[k]: continue
        visited[k] = 1
        stack.append(k)
        dfs(i+1)
        visited[k] = 0
        stack.pop()


def check(n1, op, n2):
    if op=='<':
        return n1<n2
    return n1>n2


N = int(input())
ops = list(input().split())
arr = list(range(1, 10))
visited = [0]*10
stack = []
ansLst = []
dfs(0)

print(ansLst[-1])
print(ansLst[0])
