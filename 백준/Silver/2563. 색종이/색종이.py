N = int(input())
mat = [[0]*101 for _ in range(101)]
for _ in range(N):
    x, y = map(int, input().split())
    for xx in range(x, x+10):
        for yy in range(y, y+10):
            mat[xx][yy] = 1

print(sum([sum(lst) for lst in mat]))