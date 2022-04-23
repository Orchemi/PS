def preorder(X):
    if X=='.':
        return

    print(X, end='')
    preorder(dictL[X])
    preorder(dictR[X])
    return

def inorder(X):
    if X=='.':
        return

    inorder(dictL[X])
    print(X, end='')
    inorder(dictR[X])
    return

def postorder(X):
    if X=='.':
        return

    postorder(dictL[X])
    postorder(dictR[X])
    print(X, end='')
    return


N = int(input())
dictL = {}
dictR = {}
for _ in range(N):
    v, l, r = input().split()
    dictL[v] = l
    dictR[v] = r


preorder('A')
print()
inorder('A')
print()
postorder('A')