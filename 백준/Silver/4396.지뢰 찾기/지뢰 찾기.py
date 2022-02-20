n = int(input())
matB = [list(input()) for _ in range(n)]
matP = [list(input()) for _ in range(n)]

flag = 0
for i in range(n):
    for j in range(n):
        # x라면
        if matP[i][j]=='x':
            # 해당 위치가 폭탄이 있다면
            if matB[i][j]=='*':
                flag = 1

            # 해당 위치에 폭탄이 없다면
            else:
                matP[i][j] = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if (0<=i+di<n) and (0<=j+dj<n):
                            if matB[i+di][j+dj]=='*':
                                matP[i][j]+=1

if flag:
    for i in range(n):
        for j in range(n):
            if matB[i][j]=='*':
                matP[i][j]='*'

for lst in matP:
    t = ''
    for i in lst:
        t += str(i)
    print(t)