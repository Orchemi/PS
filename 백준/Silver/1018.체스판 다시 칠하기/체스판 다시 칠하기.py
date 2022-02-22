H, W = map(int, input().split())
mat = [list(input()) for _ in range(H)]

min_v = H*W
for i in range(H-8+1):
    for j in range(W-8+1):
        cnt_a = cnt_b = 0
        for di in range(0,8,2):
            for dj in range(0,8,2):
                if mat[i+di][j+dj] == 'B':
                    cnt_a += 1
                else:
                    cnt_b += 1

            for dj in range(1,8,2):
                if mat[i+di][j+dj] == 'W':
                    cnt_a += 1
                else:
                    cnt_b += 1

        for di in range(1,8,2):
            for dj in range(1,8,2):
                if mat[i+di][j+dj] == 'B':
                    cnt_a += 1
                else:
                    cnt_b += 1

            for dj in range(0,8,2):
                if mat[i+di][j+dj] == 'W':
                    cnt_a += 1
                else:
                    cnt_b += 1

        if min_v > cnt_a:
            min_v = cnt_a
        if min_v > cnt_b:
            min_v = cnt_b

print(min_v)