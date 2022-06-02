import sys
N = int(input())
s = 0
e = 1
ssum = 1
cnt = 0

while e <= N:
    if ssum <= N:
        if ssum == N:
            cnt += 1
        e += 1
        ssum += e

    else:
        ssum -= s
        s += 1

print(cnt)