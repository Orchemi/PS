Y = list(map(int, input().split()))
G = list(map(int, input().split()))
scores = [0, 0]

won_y = False
for i in range(9):
    scores[0] += Y[i]
    if scores[0] > scores[1]:
        won_y = True
    scores[1] += G[i]

ret = 'Yes' if won_y else 'No'
print(ret)