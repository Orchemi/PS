def make(a, b, c):
    if memo[a][b][c]!=-1: pass
    elif a>70 or b>70 or c>70:
        memo[a][b][c] = make(70, 70, 70)
    elif a < b < c:
        memo[a][b][c] = make(a, b, c-1) + make(a, b-1, c-1) - make(a, b-1, c)
    else:
        memo[a][b][c] = make(a-1, b, c) + make(a-1, b-1, c) + make(a-1, b, c-1) - make(a-1, b-1, c-1)
    return memo[a][b][c]


memo = [[[1]*101 for _ in range(101)] for _ in range(101)]
for x in range(51, 101):
    for y in range(51, 101):
        for z in range(51, 101):
            memo[x][y][z] = -1


while True:
    a, b, c, = map(lambda x: int(x)+50, input().split())
    if a==b==c==49: break
    print(f'w({a-50}, {b-50}, {c-50}) = {make(a, b, c)}')