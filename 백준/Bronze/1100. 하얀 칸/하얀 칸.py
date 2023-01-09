mat = [list(input()) for _ in range(8)]
cnt = 0
for i in range(8):
    a = i%2
    for j in range(8):
        b = j%2
        if a+b!=1 and mat[i][j]=='F':
            cnt += 1

print(cnt)