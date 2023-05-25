import sys
input = sys.stdin.readline

I, J, Y, X = map(int, input().split())
II, JJ = I+Y, J+X
mat = [list(map(int, input().split())) for _ in range(II)]

ret = []
for i in range(I):
    ret.append(mat[i][:J])

si = Y
while si<I:
    sj = X
    while sj<J:
        ret[si][sj] -= ret[si-Y][sj-X]
        sj += 1
    si += 1

for l in ret:
    print(*l)