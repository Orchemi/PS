import sys
input = sys.stdin.readline

N = int(input())
S = 0
while N:
    a = input().split()
    if len(a) > 1:
        v = int(a[1])-1
    f = a[0]

    if f=='add':
        S = S|(1<<v)
    elif f=='remove':
        S = S&~(1<<v)
    elif f=='check':
        if S&(1<<v): print(1)
        else: print(0)
    elif f=='toggle':
        S = S^(1<<v)
    elif f=='all':
        S = S|1048575
    elif f=='empty':
        S = S&0
    N -= 1