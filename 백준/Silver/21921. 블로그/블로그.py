N, X = map(int, input().split())
days = list(map(int, input().split()))
maxx, cnt, i = 0, 0, 0
ssum = sum(days[:X])
while True:
    if maxx < ssum:
        cnt = 1
        maxx = ssum
    elif maxx == ssum:
        cnt += 1
    if i+X == N: break
    ssum += days[i+X]-days[i]
    i += 1

if maxx:
    print(maxx)
    print(cnt)
else:
    print('SAD')