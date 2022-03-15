N = int(input())
cnt = 0
n = 665
while cnt < N:
    txts = str(n)
    tmax = len(txts)
    ti = pi = 0

    while ti < tmax and pi < 3:
        if not txts[ti] == '6':
            pi = 0
        else:
            pi += 1
        ti += 1

    cnt = cnt+1 if pi == 3 else cnt
    n += 1

print(n-1)