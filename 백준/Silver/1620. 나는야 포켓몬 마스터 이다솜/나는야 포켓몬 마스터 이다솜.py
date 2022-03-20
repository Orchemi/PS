N, M = map(int, input().split())
dictA = {}
lstA = ['']*(N+1)

for i in range(1, N+1):
    name = input()
    dictA[name] = i
    lstA[i] = name

for _ in range(M):
    a = input()
    if a.isdecimal():
        print(lstA[int(a)])
    else:
        print(dictA[a])