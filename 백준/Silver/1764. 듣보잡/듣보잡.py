dictN = {}
N, M = map(int, input().split())
for _ in range(N):
    nameN = input()
    dictN[nameN] = 1

cnt = 0
lstNM = []
for _ in range(M):
    nameM = input()
    if dictN.get(nameM):
        cnt += 1
        lstNM.append(nameM)

lstNM.sort()
print(cnt)
for name in lstNM:
    print(name)