def calc(lst, l):
    ret = 0
    lst = [0]+lst+[0]
    for i in range(l+1):
        ret += abs(lst[i]-lst[i+1])
    return ret

I, J = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(I)]
ret = 2*I*J
for lst in mat:
    ret += calc(lst, J)

for j in range(J):
    lst = [mat[i][j] for i in range(I)]
    ret += calc(lst, I)

print(ret)