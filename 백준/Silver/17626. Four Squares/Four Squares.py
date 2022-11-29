from math import floor

def foo(depth, cnt, ssum):
    if depth==cnt-1:
        tar = (N-ssum)**0.5
        return tar == floor(tar)

    k = 1
    while ssum+k**2 <= N:
        if foo(depth+1, cnt, ssum+k**2): return 1
        k += 1
    return 0

N = int(input())
for i in range(1, 5):
    if foo(0, i, 0):
        print(i)
        quit()