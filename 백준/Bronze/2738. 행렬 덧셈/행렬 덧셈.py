I, J = map(int, input().split())
m1 = [list(map(int, input().split())) for _ in range(I)]
m2 = [list(map(int, input().split())) for _ in range(I)]

for i in range(I):
    for j in range(J):
        print(m1[i][j] + m2[i][j], end=' ')
    print()