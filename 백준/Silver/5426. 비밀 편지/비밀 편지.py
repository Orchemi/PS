N = int(input())
for _ in range(N):
    txt = input()
    l = len(txt)
    K = int(l**(1/2))

    mat = [[txt[i*K+j] for j in range(K)] for i in range(K)]
    ret = ''
    for j in range(K-1, -1, -1):
        ret += ''.join([mat[i][j] for i in range(K)])
    print(ret)